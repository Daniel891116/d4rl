#!/bin/bash

for i in {1..17}
do
    python3 scripts/generate_randMaze2d_datasets.py  --agent_centric --save_images --batch_idx=$i --data_dir=../dataset/maze_act_biased_clip_60 --clip_deg=30
done