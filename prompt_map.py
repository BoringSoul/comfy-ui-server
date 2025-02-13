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
            "frame_rate": 25,
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
    },
    "sdxl_lcm":{
        "1": {
            "inputs": {
            "seed": [
                "46",
                0
            ],
            "steps": 20,
            "cfg": 1.3,
            "sampler_name": "lcm",
            "scheduler": "normal",
            "denoise": 1,
            "model": [
                "10",
                0
            ],
            "positive": [
                "5",
                0
            ],
            "negative": [
                "5",
                1
            ],
            "latent_image": [
                "5",
                2
            ]
            },
            "class_type": "KSampler",
            "_meta": {
            "title": "K采样器"
            }
        },
        "2": {
            "inputs": {
            "min_cfg": 1,
            "model": [
                "16",
                0
            ]
            },
            "class_type": "VideoLinearCFGGuidance",
            "_meta": {
            "title": "视频线性CFG引导"
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
        "5": {
            "inputs": {
            "width": [
                "45",
                0
            ],
            "height": [
                "45",
                1
            ],
            "video_frames": 100,
            "motion_bucket_id": 192,
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
        "6": {
            "inputs": {
            "image": "IMG_0209.jpeg",
            "upload": "image"
            },
            "class_type": "LoadImage",
            "_meta": {
            "title": "加载图像"
            }
        },
        "7": {
            "inputs": {
            "samples": [
                "1",
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
        "9": {
            "inputs": {
            "frame_rate": 6,
            "loop_count": 0,
            "filename_prefix": "svd_",
            "format": "video/h264-mp4",
            "pix_fmt": "yuv420p",
            "crf": 19,
            "save_metadata": True,
            "trim_to_audio": False,
            "pingpong": True,
            "save_output": True,
            "images": [
                "7",
                0
            ]
            },
            "class_type": "VHS_VideoCombine",
            "_meta": {
            "title": "Video Combine"
            }
        },
        "10": {
            "inputs": {
            "b1": 1.3,
            "b2": 1.4,
            "s1": 0.9,
            "s2": 0.2,
            "model": [
                "2",
                0
            ]
            },
            "class_type": "FreeU_V2",
            "_meta": {
            "title": "FreeU_V2"
            }
        },
        "16": {
            "inputs": {
            "lora_name": "lcm-lora-sdxl.safetensors",
            "strength_model": 0.3,
            "strength_clip": 1,
            "model": [
                "4",
                0
            ],
            "clip": [
                "32",
                0
            ]
            },
            "class_type": "LoraLoader",
            "_meta": {
            "title": "加载LoRA"
            }
        },
        "31": {
            "inputs": {
            "ckpt_name": "SDXL/lovexlAllInOneMega_v20.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
            "_meta": {
            "title": "Checkpoint加载器（简易）"
            }
        },
        "32": {
            "inputs": {
            "stop_at_clip_layer": -2,
            "clip": [
                "31",
                1
            ]
            },
            "class_type": "CLIPSetLastLayer",
            "_meta": {
            "title": "设置CLIP最后一层"
            }
        },
        "45": {
            "inputs": {
            "resolution": "1216x832"
            },
            "class_type": "CM_SDXLResolution",
            "_meta": {
            "title": "SDXLResolution"
            }
        },
        "46": {
            "inputs": {
            "seed": 513062095366474
            },
            "class_type": "Seed Generator",
            "_meta": {
            "title": "Seed Generator"
            }
        }
    }
}

from model.req.task import PromptRequest
def get_prompt(prompt_request:PromptRequest) -> dict:
    if prompt_request.model_name == "svd":
        return handle_svd_prompt(prompt_request)
    elif prompt_request.model_name == "sdxl_lcm":
        return handle_sdxl_lcm_prompt(prompt_request)
    

def handle_svd_prompt(prompt_request:PromptRequest) -> dict:
    prompt = PROMPT_MAP.get("svd")
    prompt["6"]["inputs"]["image"] = prompt_request.image_name
    if prompt_request.width:
        prompt["1"]["inputs"]["width"] = prompt_request.width
    if prompt_request.height:
        prompt["1"]["inputs"]["height"] = prompt_request.height
    if prompt_request.video_frames:
        prompt["1"]["inputs"]["video_frames"] = prompt_request.video_frames
    if prompt_request.fps:
        prompt["1"]["inputs"]["fps"] = prompt_request.fps
    if prompt_request.steps:
        prompt["7"]["inputs"]["steps"] = prompt_request.steps
    return prompt


def handle_sdxl_lcm_prompt(prompt_request:PromptRequest) -> dict:
    prompt = PROMPT_MAP.get("sdxl_lcm")
    prompt["6"]["inputs"]["image"] = prompt_request.image_name
    if prompt_request.video_frames:
        prompt["5"]["inputs"]["video_frames"] = prompt_request.video_frames
    if prompt_request.fps:
        prompt["5"]["inputs"]["fps"] = prompt_request.fps
    if prompt_request.steps:
        prompt["1"]["inputs"]["steps"] = prompt_request.steps