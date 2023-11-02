#!/bin/bash

for i in {1..8}
do
    (python3 scripts/generate_randMaze2d_datasets.py  --agent_centric --save_images --batch_idx=$i --data_dir=../dataset/maze_act_biased_120deg --clip_deg=60) &
done