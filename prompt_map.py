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
            "steps": 10,
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
            "video_frames": 25,
            "motion_bucket_id": 192,
            "fps": 6,
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
            "image": "SABC.jpeg",
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
            "save_output": False,
            "images": [
                "7",
                0
            ]
            },
            "class_type": "VHS_VideoCombine",
            "_meta": {
            "title": "Video Combine 🎥🅥🅗🅢"
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
            "strength_model": 1,
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
            "seed": 153186343832434
            },
            "class_type": "Seed Generator",
            "_meta": {
            "title": "Seed Generator"
            }
        }
    },
    "clay_svd": {
        "1": {
            "inputs": {
            "detect_hand": "disable",
            "detect_body": "enable",
            "detect_face": "disable",
            "resolution": 512,
            "scale_stick_for_xinsr_cn": "disable",
            "image": [
                "17",
                0
            ]
            },
            "class_type": "OpenposePreprocessor",
            "_meta": {
            "title": "OpenPose Pose"
            }
        },
        "2": {
            "inputs": {
            "text": [
                "12",
                0
            ],
            "clip": [
                "15",
                1
            ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
            "title": "CLIP文本编码"
            }
        },
        "3": {
            "inputs": {
            "pixels": [
                "17",
                0
            ],
            "vae": [
                "14",
                2
            ]
            },
            "class_type": "VAEEncode",
            "_meta": {
            "title": "VAE编码"
            }
        },
        "4": {
            "inputs": {
            "samples": [
                "5",
                0
            ],
            "vae": [
                "14",
                2
            ]
            },
            "class_type": "VAEDecode",
            "_meta": {
            "title": "VAE解码"
            }
        },
        "5": {
            "inputs": {
            "seed": 405155855046177,
            "steps": 35,
            "cfg": 7,
            "sampler_name": "dpmpp_2m",
            "scheduler": "karras",
            "denoise": 0.65,
            "model": [
                "15",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "negative": [
                "6",
                1
            ],
            "latent_image": [
                "3",
                0
            ]
            },
            "class_type": "KSampler",
            "_meta": {
            "title": "K采样器"
            }
        },
        "6": {
            "inputs": {
            "switch": "On",
            "base_positive": [
                "2",
                0
            ],
            "base_negative": [
                "9",
                0
            ],
            "controlnet_stack": [
                "13",
                0
            ]
            },
            "class_type": "CR Apply Multi-ControlNet",
            "_meta": {
            "title": "🕹️ CR Apply Multi-ControlNet"
            }
        },
        "7": {
            "inputs": {
            "preprocessor": "DepthAnythingPreprocessor",
            "resolution": 512,
            "image": [
                "17",
                0
            ]
            },
            "class_type": "AIO_Preprocessor",
            "_meta": {
            "title": "AIO Aux Preprocessor"
            }
        },
        "8": {
            "inputs": {
            "preprocessor": "LineArtPreprocessor",
            "resolution": 512,
            "image": [
                "17",
                0
            ]
            },
            "class_type": "AIO_Preprocessor",
            "_meta": {
            "title": "AIO Aux Preprocessor"
            }
        },
        "9": {
            "inputs": {
            "text": "text, watermark,embedding:JuggernautNegative-neg, ",
            "clip": [
                "15",
                1
            ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
            "title": "CLIP文本编码"
            }
        },
        "11": {
            "inputs": {
            "model": "wd-v1-4-moat-tagger-v2",
            "threshold": 0.35,
            "character_threshold": 0.85,
            "replace_underscore": False,
            "trailing_comma": False,
            "exclude_tags": "",
            "tags": "1girl, looking_at_viewer, smile, shirt, black_hair, 1boy, holding, sitting, jacket, white_shirt, glasses, solo_focus, indoors, nail_polish, head_tilt, v, phone, table, cellphone, smartphone, pink_nails, holding_phone, realistic, restaurant",
            "image": [
                "17",
                0
            ]
            },
            "class_type": "WD14Tagger|pysssss",
            "_meta": {
            "title": "WD14 Tagger 🐍"
            }
        },
        "12": {
            "inputs": {
            "text1": "",
            "text2": [
                "11",
                0
            ],
            "separator": ""
            },
            "class_type": "CR Text Concatenate",
            "_meta": {
            "title": "🔤 CR Text Concatenate"
            }
        },
        "13": {
            "inputs": {
            "switch_1": "On",
            "controlnet_1": "control-lora-depth-rank256.safetensors",
            "controlnet_strength_1": 0.6,
            "start_percent_1": 0,
            "end_percent_1": 0.6,
            "switch_2": "On",
            "controlnet_2": "control-lora-canny-rank256.safetensors",
            "controlnet_strength_2": 0.8,
            "start_percent_2": 0,
            "end_percent_2": 0.6,
            "switch_3": "On",
            "controlnet_3": "control-lora-openposeXL2-rank256.safetensors",
            "controlnet_strength_3": 0.6,
            "start_percent_3": 0,
            "end_percent_3": 0.6,
            "image_1": [
                "7",
                0
            ],
            "image_2": [
                "8",
                0
            ],
            "image_3": [
                "1",
                0
            ]
            },
            "class_type": "CR Multi-ControlNet Stack",
            "_meta": {
            "title": "🕹️ CR Multi-ControlNet Stack"
            }
        },
        "14": {
            "inputs": {
            "ckpt_name": "SDXL/juggernautXL_v9Rdphoto2Lightning.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
            "_meta": {
            "title": "Checkpoint加载器（简易）"
            }
        },
        "15": {
            "inputs": {
            "lora_name": {
                "content": "CLAYMATE_V2.03_.safetensors",
                "image": null
            },
            "strength_model": 1,
            "strength_clip": 1,
            "example": "[none]",
            "model": [
                "14",
                0
            ],
            "clip": [
                "14",
                1
            ]
            },
            "class_type": "LoraLoader|pysssss",
            "_meta": {
            "title": "Lora Loader 🐍"
            }
        },
        "16": {
            "inputs": {
            "purge_cache": True,
            "purge_models": True,
            "anything": [
                "4",
                0
            ]
            },
            "class_type": "LayerUtility: PurgeVRAM",
            "_meta": {
            "title": "LayerUtility: Purge VRAM"
            }
        },
        "17": {
            "inputs": {
            "image": "1.jpeg",
            "upload": "image"
            },
            "class_type": "LoadImage",
            "_meta": {
            "title": "加载图像"
            }
        },
        "20": {
            "inputs": {
            "min_cfg": 1,
            "model": [
                "22",
                0
            ]
            },
            "class_type": "VideoLinearCFGGuidance",
            "_meta": {
            "title": "视频线性CFG引导"
            }
        },
        "21": {
            "inputs": {
            "samples": [
                "23",
                0
            ],
            "vae": [
                "22",
                2
            ]
            },
            "class_type": "VAEDecode",
            "_meta": {
            "title": "VAE解码"
            }
        },
        "22": {
            "inputs": {
            "ckpt_name": "svd/svd_xt.safetensors"
            },
            "class_type": "ImageOnlyCheckpointLoader",
            "_meta": {
            "title": "Checkpoint加载器（仅图像）"
            }
        },
        "23": {
            "inputs": {
            "seed": 424113688994927,
            "steps": 20,
            "cfg": 3,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1,
            "model": [
                "20",
                0
            ],
            "positive": [
                "24",
                0
            ],
            "negative": [
                "24",
                1
            ],
            "latent_image": [
                "24",
                2
            ]
            },
            "class_type": "KSampler",
            "_meta": {
            "title": "K采样器"
            }
        },
        "24": {
            "inputs": {
            "width": 1024,
            "height": 576,
            "video_frames": 100,
            "motion_bucket_id": 100,
            "fps": 25,
            "augmentation_level": 0,
            "clip_vision": [
                "22",
                1
            ],
            "init_image": [
                "4",
                0
            ],
            "vae": [
                "22",
                2
            ]
            },
            "class_type": "SVD_img2vid_Conditioning",
            "_meta": {
            "title": "SVD_img2vid条件"
            }
        },
        "25": {
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
                "21",
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

from model.req.task import PromptRequest
def get_prompt(prompt_request:PromptRequest) -> dict:
    if prompt_request.model_name == "svd":
        return handle_svd_prompt(prompt_request)
    elif prompt_request.model_name == "sdxl_lcm":
        return handle_sdxl_lcm_prompt(prompt_request)
    elif prompt_request.model_name == "clay_svd":
        return handle_clay_svd(prompt_request)
    

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
    return prompt

def handle_clay_svd(prompt_request:PromptRequest) -> dict:
    prompt = PROMPT_MAP.get("clay_svd")
    prompt["17"]["inputs"]["image"] = prompt_request.image_name
    if prompt_request.video_frames:
        prompt["24"]["inputs"]["video_frames"] = prompt_request.video_frames
    if prompt_request.fps:
        prompt["24"]["inputs"]["fps"] = prompt_request.fps
    if prompt_request.steps:
        prompt["23"]["inputs"]["steps"] = prompt_request.steps
    return prompt