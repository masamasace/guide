---
title: "Blenderの基本的な使用方法"
date: "2024-03-22"
---

## 公式ダウンロード元
- 

## 魚眼レンズへの設定
- まずレンダリングエンジンをCyclesに変更する必要がある
    - https://www.reddit.com/r/blenderhelp/comments/11f6r7h/why_isnt_the_panorama_type_showing_up_in_my/
    - BlenderにはEEVEEとCyclesという2つのレンダリングエンジンがある
        - 違いについてはよくわかっていない
    - 初期画面の右側>上から2つ目の後ろからのカメラのアイコン(Render)>Render Engine>Cyclesに変更
    - Edit>PreferencesでPreferencesの画面に入る
    - 左側下から3つ目のSystemでCUDAを選択し，搭載されているGPUにチェックマークをいれる
- 初期画面の右側>下から2つ目の映画用カメラの横からのアイコン(Camera)>Lens>Type>Panoramicに変更
- 