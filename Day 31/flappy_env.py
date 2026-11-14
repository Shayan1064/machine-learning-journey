
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame


class FlappyBirdEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super().__init__()

        self.render_mode = render_mode
        self.width = 400
        self.height = 600

        self.bird_x = 80
        self.bird_radius = 12

        # Easier physics for learning
        self.gravity = 0.35
        self.flap_strength = -6.0
        self.max_velocity = 8.0

        self.pipe_width = 60
        self.pipe_gap = 220
        self.pipe_speed = 2.5

        # 0 = do nothing, 1 = flap
        self.action_space = spaces.Discrete(2)

        # Bird height, velocity, pipe distance,
        # top of gap, bottom of gap
        self.observation_space = spaces.Box(
            low=np.array([0, -1, -1, 0, 0], dtype=np.float32),
            high=np.array([1, 1, 1, 1, 1], dtype=np.float32),
            dtype=np.float32,
        )

        self.screen = None
        self.clock = None

        self.reset()

    def _get_obs(self):
        gap_top = self.gap_y - self.pipe_gap / 2
        gap_bottom = self.gap_y + self.pipe_gap / 2
        distance = self.pipe_x - self.bird_x

        # Normalize inputs so the neural network learns more easily
        return np.array(
            [
                np.clip(self.bird_y / self.height, 0, 1),
                np.clip(self.bird_velocity / self.max_velocity, -1, 1),
                np.clip(distance / self.width, -1, 1),
                gap_top / self.height,
                gap_bottom / self.height,
            ],
            dtype=np.float32,
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.bird_y = self.height / 2
        self.bird_velocity = 0.0

        self.pipe_x = self.width
        self.gap_y = self.np_random.uniform(
            150, self.height - 150
        )

        self.passed_pipe = False
        self.steps = 0

        return self._get_obs(), {}

    def step(self, action):
        self.steps += 1

        if action == 1:
            self.bird_velocity = self.flap_strength

        self.bird_velocity = min(
            self.bird_velocity + self.gravity,
            self.max_velocity,
        )
        self.bird_y += self.bird_velocity
        self.pipe_x -= self.pipe_speed

        # Small reward for every surviving step
        reward = 0.1
        terminated = False

        # Hit the ceiling or floor
        if (
            self.bird_y - self.bird_radius <= 0
            or self.bird_y + self.bird_radius >= self.height
        ):
            reward = -5.0
            terminated = True

        gap_top = self.gap_y - self.pipe_gap / 2
        gap_bottom = self.gap_y + self.pipe_gap / 2

        # Check collision with the pipe
        pipe_overlap = (
            self.pipe_x < self.bird_x + self.bird_radius
            and self.pipe_x + self.pipe_width
            > self.bird_x - self.bird_radius
        )

        if pipe_overlap and (
            self.bird_y - self.bird_radius < gap_top
            or self.bird_y + self.bird_radius > gap_bottom
        ):
            reward = -5.0
            terminated = True

        # Reward successfully passing a pipe
        if (
            not terminated
            and not self.passed_pipe
            and self.pipe_x + self.pipe_width
            < self.bird_x - self.bird_radius
        ):
            reward += 10.0
            self.passed_pipe = True

        # Place the next pipe
        if self.pipe_x + self.pipe_width < 0:
            self.pipe_x = self.width
            self.gap_y = self.np_random.uniform(
                150, self.height - 150
            )
            self.passed_pipe = False

        truncated = self.steps >= 3000

        if self.render_mode == "human":
            self.render()

        return self._get_obs(), reward, terminated, truncated, {}

    def render(self):
        if self.screen is None:
            pygame.init()
            self.screen = pygame.display.set_mode(
                (self.width, self.height)
            )
            pygame.display.set_caption("Flappy Bird AI")
            self.clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                return

        self.screen.fill((135, 206, 235))

        # Draw bird
        pygame.draw.circle(
            self.screen,
            (255, 220, 0),
            (self.bird_x, int(self.bird_y)),
            self.bird_radius,
        )

        # Draw pipes
        gap_top = int(self.gap_y - self.pipe_gap / 2)
        gap_bottom = int(self.gap_y + self.pipe_gap / 2)

        pygame.draw.rect(
            self.screen,
            (0, 180, 0),
            (int(self.pipe_x), 0, self.pipe_width, gap_top),
        )

        pygame.draw.rect(
            self.screen,
            (0, 180, 0),
            (
                int(self.pipe_x),
                gap_bottom,
                self.pipe_width,
                self.height - gap_bottom,
            ),
        )

        pygame.display.flip()
        self.clock.tick(self.metadata["render_fps"])

    def close(self):
        if self.screen is not None:
            pygame.display.quit()
            pygame.quit()
            self.screen = None
            self.clock = None
