import chess
#import chess.svg
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class ChessEnvironment:
    def __init__(self):
        self.board = chess.Board()

    def reset(self):
        self.board = chess.Board()

    def get_state(self):
        return np.array(self.board.fen())

    def step(self, action):
        move = chess.Move.from_uci(action)
        if move in self.board.legal_moves:
            self.board.push(move)
            done = self.board.is_game_over()
            reward = 1.0 if done and self.board.result() == "1-0" else 0.0
            return self.get_state(), reward, done
        else:
            # Invalid move, penalize the agent
            return self.get_state(), -0.1, False

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=0.001))
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(range(self.action_size))
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# Main training loop
env = ChessEnvironment()
state_size = len(env.get_state())
action_size = 1968  # Number of possible chess moves (7 * 7 * 6 * 7)

agent = DQNAgent(state_size, action_size)

for episode in range(1000):
    state = env.get_state()
    state = np.reshape(state, [1, state_size])
    total_reward = 0
    done = False

    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward

    print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

    if len(agent.memory) > 32:
        agent.replay(32)
