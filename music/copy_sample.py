import os

def read_list(fname):
    result = []
    with open(fname, "r") as f:
        for each in f.readlines():
            each = each.strip('\n')
            result.append(each)
    return result

result_path = "/mnt/bn/lqhaoheliu/project/audio_generation_diffusion/log/audiomae_pred/19_2_overall_pretrain_gpt2_foundation/2023_07_24_full_8_ft_ddpm_crossattn_t5_music/val_0_07-26-17:16_cfg_scale_3.5_ddim_200_n_cand_3"
target_cp_path = "/mnt/bn/lqhaoheliu/hhl_script2/2023/ICLR/MOS_Music/2023_07_24_full_8_ft_ddpm_crossattn_t5_music"

# result_path = "/mnt/bn/lqhaoheliu/project/audio_generation_diffusion/log/testset_data/audiocaps_16k"
# target_cp_path = "/mnt/bn/lqhaoheliu/hhl_script2/2023/ICLR/MOS_Audio/groundtruth"

# result_path = "/mnt/bn/lqhaoheliu/project/audio_generation_diffusion/log/latent_diffusion/30_final_audiocaps_baseline/2023_07_16_small_8_crossattn/val_278461_07-22-14:08_cfg_scale_3.5_ddim_200_n_cand_3"
# target_cp_path = "/mnt/bn/lqhaoheliu/hhl_script2/2023/ICLR/MOS_Audio/audiobox"

filelist = read_list("/mnt/bn/lqhaoheliu/hhl_script2/2023/ICLR/MOS_Music/filename_v2.lst")

for file in filelist:
    audiofile_path = os.path.join(result_path, file)
    if(os.path.exists(audiofile_path)):
        cmd = "cp %s %s" % (audiofile_path, target_cp_path)
        os.system(cmd)
    else:
        raise ValueError("File %s not found" % file)