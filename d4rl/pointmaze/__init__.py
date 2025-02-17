from .maze_layouts import OPEN, U_MAZE, MEDIUM_MAZE, LARGE_MAZE, U_MAZE_EVAL, MEDIUM_MAZE_EVAL, LARGE_MAZE_EVAL, \
            HARD_EXP_MAZE, HARD_EXP_MAZE_V2, rand_layout, \
            SCRL_20_TEST_V0,\
            SCRL_20_GO_LEFT_V0, SCRL_20_GO_LEFT_V1, SCRL_20_GO_LEFT_V2,\
            SCRL_20_GO_RIGHT_V0,\
            SCRL_20_GO_UP_V0,\
            SCRL_20_GO_DOWN_V0
from .maze_model import MazeEnv
from .semantic_maze_layouts import SEMANTIC_MAZE_LAYOUTS, semantic_layout2str

from gym.envs.registration import register

register(
    id='maze2d-open-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':OPEN,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 0.01,
        'ref_max_score': 20.66,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-sparse.hdf5'
    }
)

register(
    id='maze2d-umaze-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 0.94,
        'ref_max_score': 62.6,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-sparse.hdf5'
    }
)

register(
    id='maze2d-medium-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=250,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 5.77,
        'ref_max_score': 85.14,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse.hdf5'
    }
)


register(
    id='maze2d-large-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse.hdf5'
    }
)


register(
    id='maze2d-umaze-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 23.85,
        'ref_max_score': 161.86,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-medium-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 13.13,
        'ref_max_score': 277.39,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-large-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 6.7,
        'ref_max_score': 273.99,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-eval-umaze-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 36.63,
        'ref_max_score': 141.4,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-umaze-sparse-v1.hdf5'
    }
)

register(
    id='maze2d-eval-medium-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 13.07,
        'ref_max_score': 204.93,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-medium-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-eval-large-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE_EVAL,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 16.4,
        'ref_max_score': 302.22,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-large-sparse-v1.hdf5'
    }
)


register(
    id='maze2d-hardexp-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':HARD_EXP_MAZE,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexp-sparse.hdf5'
    }
)


register(
    id='maze2d-hardexp-v2',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':HARD_EXP_MAZE_V2,
        'reward_type':'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-hardexp-agent_centric-v2',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': HARD_EXP_MAZE_V2,
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze0-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=0),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze1-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=1),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze42-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=42),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze0S30-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=0, size=30),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze0S30-ac-render-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=0, size=30),
        'agent_centric_view': False,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze0S40-ac-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=0, size=40),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze1010-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=1, size=10),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


register(
    id='maze2d-randMaze2020-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': rand_layout(seed=0, size=20),
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-render-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V0,
        'agent_centric_view': False,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V0,
        'agent_centric_view': True,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-sparse-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V0,
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        # 'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-render-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V0,
        'agent_centric_view': False,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        # 'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V0,
        'agent_centric_view': True,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-dense-v2',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V1,
        'agent_centric_view': True,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-render-v2',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V1,
        'agent_centric_view': False,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-dense-v3',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V2,
        'agent_centric_view': True,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-render-v3',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_LEFT_V2,
        'agent_centric_view': False,
        'reward_type': 'dense',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-sparse-go-right-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_RIGHT_V0,
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-sparse-go-up-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_UP_V0,
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-SCRL2020-sparse-go-down-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': SCRL_20_GO_DOWN_V0,
        'agent_centric_view': True,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

##################### SEMANTIC MAZE LAYOUTS #############
register(
    id='maze2d-semanticMaze1-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': semantic_layout2str(SEMANTIC_MAZE_LAYOUTS[1][0]),
        'agent_centric_view': False,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)

register(
    id='maze2d-semanticMaze2-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec': semantic_layout2str(SEMANTIC_MAZE_LAYOUTS[2][0]),
        'agent_centric_view': False,
        'reward_type': 'sparse',
        'reset_target': False,
        'ref_min_score': 4.83,
        'ref_max_score': 191.99,
        'dataset_url':'http://maze2d-hardexpv2-sparse.hdf5'
    }
)


##################### OLD LAYOUTS #######################

register(
    id='maze2d-open-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':OPEN,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 11.17817,
        'ref_max_score': 27.166538620695782,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-open-dense.hdf5'
    }
)

register(
    id='maze2d-umaze-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=150,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 23.249793,
        'ref_max_score': 81.78995240126592,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-dense.hdf5'
    }
)

register(
    id='maze2d-medium-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=250,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 19.477620,
        'ref_max_score': 96.03474232952358,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-dense.hdf5'
    }
)


register(
    id='maze2d-large-dense-v0',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 27.388310,
        'ref_max_score': 215.09965671563742,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-dense.hdf5'
    }
)

register(
    id='maze2d-umaze-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 68.537689,
        'ref_max_score': 193.66285642381482,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-umaze-dense-v1.hdf5'
    }
)

register(
    id='maze2d-medium-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 44.264742,
        'ref_max_score': 297.4552547777125,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-dense-v1.hdf5'
    }
)


register(
    id='maze2d-large-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 30.569041,
        'ref_max_score': 303.4857382709002,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-dense-v1.hdf5'
    }
)

register(
    id='maze2d-eval-umaze-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=300,
    kwargs={
        'maze_spec':U_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 56.95455,
        'ref_max_score': 178.21373133248397,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-umaze-dense-v1.hdf5'
    }
)

register(
    id='maze2d-eval-medium-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=600,
    kwargs={
        'maze_spec':MEDIUM_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 42.28578,
        'ref_max_score': 235.5658957482388,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-medium-dense-v1.hdf5'
    }
)


register(
    id='maze2d-eval-large-dense-v1',
    entry_point='d4rl.pointmaze:MazeEnv',
    max_episode_steps=800,
    kwargs={
        'maze_spec':LARGE_MAZE_EVAL,
        'reward_type':'dense',
        'reset_target': False,
        'ref_min_score': 56.95455,
        'ref_max_score': 326.09647655082637,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-eval-large-dense-v1.hdf5'
    }
)
