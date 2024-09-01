<img src="https://github.com/devch1013/YAICON-VGGnet/assets/92439610/0ce35aae-3e19-4a7c-9ea2-0fd8434a6edb" width = "900" >

# VGGnet: Video Graphic Generation network (Dec. 2023)

## 🥉 3rd YAICON Novelty Prize!!
<a href="https://y-ai.notion.site/VGGNet-c23ed35acaee4e13b2c088dce67d0cad">
    <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion" alt="Notion" />
</a>  
<a href="https://www.instagram.com/p/C0gditMvuZ2/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram" alt="Instagram" />
</a> 

## Members 
- 박찬혁: PM, AI lead
- 최가윤: AI
- 박승호: AI 
- 유선재: Data
- 제갈건: Data
  
---
</br>
</br>

**This is an attempt to combine the video generation model with ImageBind to create a pipeline that can generate video even with multimodal input.**

## 1. Dataset
We prepare text-text, image-text, audio-text dataset to generate embedding pair of ImageBind and T5 embedding model.


## 2. Mapping Model

## Train
```
python -m embedding.mapper_train
```

## Inference
Change the promts to text or image path or audio path.  
You can download our trained weight in models folder using this [link](https://huggingface.co/devch1013/VGGnet/tree/main).
```
python -m run_inference
```








