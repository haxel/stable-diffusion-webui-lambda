import os
os.system(f"git lfs install")
os.system(f"git clone -b v2.2 https://github.com/camenduru/stable-diffusion-webui /home/demo/source/stable-diffusion-webui")
os.chdir(f"/home/demo/source/stable-diffusion-webui")

os.system(f"git clone https://huggingface.co/embed/negative /home/demo/source/stable-diffusion-webui/embeddings/negative")
os.system(f"git clone https://huggingface.co/embed/lora /home/demo/source/stable-diffusion-webui/models/Lora/positive")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /home/demo/source/stable-diffusion-webui/models/ESRGAN -o 4x-UltraSharp.pth")
os.system(f"wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /home/demo/source/stable-diffusion-webui/scripts/run_n_times.py")
os.system(f"git clone https://github.com/deforum-art/deforum-for-automatic1111-webui /home/demo/source/stable-diffusion-webui/extensions/deforum-for-automatic1111-webui")
os.system(f"git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser")
os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface")
os.system(f"git clone https://github.com/camenduru/sd-civitai-browser /home/demo/source/stable-diffusion-webui/extensions/sd-civitai-browser")
os.system(f"git clone https://github.com/kohya-ss/sd-webui-additional-networks /home/demo/source/stable-diffusion-webui/extensions/sd-webui-additional-networks")
os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet")
os.system(f"git clone https://github.com/fkunn1326/openpose-editor /home/demo/source/stable-diffusion-webui/extensions/openpose-editor")
os.system(f"git clone https://github.com/jexom/sd-webui-depth-lib /home/demo/source/stable-diffusion-webui/extensions/sd-webui-depth-lib")
os.system(f"git clone https://github.com/hnmr293/posex /home/demo/source/stable-diffusion-webui/extensions/posex")
# os.system(f"git clone https://github.com/nonnonstop/sd-webui-3d-open-pose-editor /home/demo/source/stable-diffusion-webui/extensions/sd-webui-3d-open-pose-editor")
os.system(f"git clone https://github.com/camenduru/sd-webui-tunnels /home/demo/source/stable-diffusion-webui/extensions/sd-webui-tunnels")
os.system(f"git clone https://github.com/etherealxx/batchlinks-webui /home/demo/source/stable-diffusion-webui/extensions/batchlinks-webui")
os.system(f"git clone https://github.com/catppuccin/stable-diffusion-webui /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-catppuccin")
os.system(f"git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-locon /home/demo/source/stable-diffusion-webui/extensions/a1111-sd-webui-locon")
os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-rembg")
os.system(f"git clone https://github.com/ashen-sensored/stable-diffusion-webui-two-shot /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-two-shot")
os.system(f"git clone https://github.com/camenduru/sd_webui_stealth_pnginfo /home/demo/source/stable-diffusion-webui/extensions/sd_webui_stealth_pnginfo")
os.system(f"git clone -b dev https://github.com/camenduru/sd-webui-aspect-ratio-helper /home/demo/source/stable-diffusion-webui/extensions/sd-webui-aspect-ratio-helper")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_mlsd_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_normalbae_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_seg_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1e_sd15_tile_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.yaml")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_style_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_style_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_sketch_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_sketch_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_seg_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_seg_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_openpose_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_openpose_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_keypose_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_keypose_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_depth_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_depth_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_color_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_color_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_canny_sd14v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_canny_sd14v1.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_canny_sd15v2.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_canny_sd15v2.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_depth_sd15v2.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_depth_sd15v2.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_sketch_sd15v2.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_sketch_sd15v2.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_zoedepth_sd15v1.pth -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o t2iadapter_zoedepth_sd15v1.pth")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/dark-sushi-25d/resolve/main/darkSushi25D25D_v20.safetensors -d /home/demo/source/stable-diffusion-webui/models/Stable-diffusion -o darkSushi25D25D_v20.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt -d /home/demo/source/stable-diffusion-webui/models/Stable-diffusion -o darkSushi25D25D_v20.vae.pt")

os.system(f"sed -i -e 's/\"sd_model_checkpoint\"\,/\"sd_model_checkpoint\,sd_vae\,CLIP_stop_at_last_layers\"\,/g' /home/demo/source/stable-diffusion-webui/modules/shared.py")

os.system(f"python launch.py --port 8266 --listen --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue")