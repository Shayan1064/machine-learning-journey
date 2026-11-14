
from pathlib import Path

from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env

from flappy_env import FlappyBirdEnv


MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

env = FlappyBirdEnv()

print("Checking the game environment...")
check_env(env, warn=True)

print("Creating the DQN agent...")

model = DQN(
    "MlpPolicy",
    env,
    learning_rate=0.0001,
    buffer_size=50_000,
    learning_starts=5_000,
    batch_size=64,
    gamma=0.99,
    train_freq=4,
    gradient_steps=1,
    exploration_fraction=0.4,
    exploration_final_eps=0.03,
    target_update_interval=1_000,
    policy_kwargs={"net_arch": [128, 128]},
    verbose=1,
    device="cpu",
)

try:
    print("Training the improved Flappy Bird AI...")

    model.learn(
        total_timesteps=300_000,
        progress_bar=False,
    )

    model.save(str(MODEL_DIR / "flappy_dqn"))

    print("Training complete!")
    print(f"Model saved to: {MODEL_DIR / 'flappy_dqn.zip'}")

finally:
    env.close()
