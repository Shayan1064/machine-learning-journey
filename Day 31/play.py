
from pathlib import Path
import time

from stable_baselines3 import DQN

from flappy_env import FlappyBirdEnv


MODEL_PATH = Path("models/flappy_dqn.zip")


def main():
    if not MODEL_PATH.exists():
        print("Trained model not found!")
        print("Run train.py first to train and save the model.")
        return

    env = FlappyBirdEnv(render_mode="human")
    model = DQN.load(str(MODEL_PATH), device="cpu")

    obs, info = env.reset()
    episode = 1
    total_reward = 0.0

    try:
        while True:
            action, _states = model.predict(obs, deterministic=True)

            obs, reward, terminated, truncated, info = env.step(
                int(action)
            )
            total_reward += reward

            # Restart after each game
            if terminated or truncated:
                print(
                    f"Episode {episode} | "
                    f"Score/reward: {total_reward:.2f}"
                )
                episode += 1
                total_reward = 0.0
                obs, info = env.reset()

                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nGame stopped by user.")

    finally:
        env.close()


if __name__ == "__main__":
    main()
