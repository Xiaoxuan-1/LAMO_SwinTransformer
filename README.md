--------------------

由于github上传限制，较大的文件如Swin_Transformer权重文件、训练10个epoch所生成的模型文件以及原始光谱fits数据及其生成的png图片数据集，在这里均未上传，仅上传test.csv,LLM_test.csv文件供测评使用，后期会尝试将这些文件陆续补全。

------------------
Swin Transformer 实现星系分类
test.csv  测试文件


------------------------
基于多模态大模型实现星系分类
LLM_test.csv  多模态大模型生存的测试文件

微调命令：
NPROC_PER_NODE=4 CUDA_VISIBLE_DEVICES=0,1,2,3 swift sft --model_type deepseek-vl-7b-chat --model_id_or_path /home/hoo/.cache/modelscope/hub/deepseek-ai/deepseek-vl-7b-chat/ --custom_train_dataset_path /data/smf/LAMO_swin_transformer/dataset/train.json --lora_target_modules ALL --sft_type lora --deepspeed default-zero2 --num_train_epochs 3 --train_dataset_sample -1 --dataset_test_ratio 0.0 --quantization 4 --batch_size 8 --eval_steps 1000

推理命令：
CUDA_VISIBLE_DEVICES=0 swift infer --ckpt_dir '/data/solarLLM/output/deepseek-vl-7b-chat/v11-20240507-185808/checkpoint-9375' --load_dataset_config true --custom_val_dataset_path '/data/smf/LAMO_swin_transformer/dataset/test.json' --val_dataset_sample -1
