PROMPT_MAP = {
    "svd": {
        "1": {
            "inputs": {
            "width": 1024,
            "height": 576,
            "video_frames": 100,
            "motion_bucket_id": 100,
            "fps": 25,
            "augmentation_level": 0,
            "clip_vision": [
                "4",
                1
            ],
            "init_image": [
                "6",
                0
            ],
            "vae": [
                "4",
                2
            ]
            },
            "class_type": "SVD_img2vid_Conditioning",
            "_meta": {
            "title": "SVD_img2vid条件"
            }
        },
        "4": {
            "inputs": {
            "ckpt_name": "svd/svd_xt.safetensors"
            },
            "class_type": "ImageOnlyCheckpointLoader",
            "_meta": {
            "title": "Checkpoint加载器（仅图像）"
            }
        },
        "6": {
            "inputs": {
            "image": "example.png",
            "upload": "image"
            },
            "class_type": "LoadImage",
            "_meta": {
            "title": "加载图像"
            }
        },
        "7": {
            "inputs": {
            "seed": 1016580174406278,
            "steps": 20,
            "cfg": 3,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1,
            "model": [
                "8",
                0
            ],
            "positive": [
                "1",
                0
            ],
            "negative": [
                "1",
                1
            ],
            "latent_image": [
                "1",
                2
            ]
            },
            "class_type": "KSampler",
            "_meta": {
            "title": "K采样器"
            }
        },
        "8": {
            "inputs": {
            "min_cfg": 1,
            "model": [
                "4",
                0
            ]
            },
            "class_type": "VideoLinearCFGGuidance",
            "_meta": {
            "title": "视频线性CFG引导"
            }
        },
        "9": {
            "inputs": {
            "samples": [
                "7",
                0
            ],
            "vae": [
                "4",
                2
            ]
            },
            "class_type": "VAEDecode",
            "_meta": {
            "title": "VAE解码"
            }
        },
        "10": {
            "inputs": {
            "frame_rate": 8,
            "loop_count": 0,
            "filename_prefix": "svd",
            "format": "video/h264-mp4",
            "pix_fmt": "yuv420p",
            "crf": 19,
            "save_metadata": True,
            "trim_to_audio": False,
            "pingpong": False,
            "save_output": True,
            "images": [
                "9",
                0
            ]
            },
            "class_type": "VHS_VideoCombine",
            "_meta": {
            "title": "Video Combine"
            }
        }
    }
}

from model.request.task import PromptRequest
def get_prompt(prompt_request:PromptRequest) -> dict:
    prompt = PROMPT_MAP.get(prompt_request.model_name)
    prompt["6"]["image"] = prompt_request.image_name
    if prompt_request.width:
        prompt["6"]["width"] = prompt_request.width
    if prompt_request.height:
        prompt["6"]["height"] = prompt_request.height
    if prompt_request.video_frames:
        prompt["1"]["video_frames"] = prompt_request.video_frames
    if prompt_request.fps:
        prompt["1"]["fps"] = prompt_request.fps
    if prompt_request.steps:
        prompt["7"]["steps"] = prompt_request.steps
    return prompt
