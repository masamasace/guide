---
title: "Blenderの基本的な使用方法"
date: "2024-03-22"
---

## 公式ダウンロード元
- 

## 物体の連続配置
### Array Modifierの適用
- 左上のModelingをクリック
- 右側のスパナ(Modifiers)をクリック
- Add Modifiersをクリック
- Arrayをクリック
- パラメータを設定
- もう一度Array Modifiersをクリックすることで重ねがけも可能
- 終わったらObjectモードにした状態でカメラの横にある下三角のマークをクリックして，Applyする

### 物体をバラバラにする
- 参考URL：https://blender.stackexchange.com/questions/109/how-can-i-use-an-array-modifier-to-create-individually-manipulatable-objects
- 複製が終わったらEdit Modeに入り，複製した物体をすべて選択する
- キーボードのpを押し，出てきたウインドウのSeperate by Loose Partsを押す
- Object Modeに入り，左上のObject>SEt Origin>Origin to Geometryを押す
    - こうすることでそれぞれの物体の初期位置が原点となった状態で物体が配置される


## 魚眼レンズへの設定
- まずレンダリングエンジンをCyclesに変更する必要がある
    - https://www.reddit.com/r/blenderhelp/comments/11f6r7h/why_isnt_the_panorama_type_showing_up_in_my/
    - BlenderにはEEVEEとCyclesという2つのレンダリングエンジンがある
        - 違いについてはよくわかっていない
    - 初期画面の右側>上から2つ目の後ろからのカメラのアイコン(Render)>Render Engine>Cyclesに変更
    - Edit>PreferencesでPreferencesの画面に入る
    - 左側下から3つ目のSystemでCUDAを選択し，搭載されているGPUにチェックマークをいれる
- 初期画面の右側>下から2つ目の映画用カメラの横からのアイコン(Camera)>Lens>Type>Panoramicに変更
    - Panorama Typeで色々選択できる
    - 目的に一番近そうなFisheye Lens Polynomialを選択
        - パラメータを変える
- 画面右上のテカテカしたボールのアイコン(Viewport Shading)をクリック
    - すると簡易的なレンダリングの結果が表示される．パラメータを変えるとレンダリング画像が変わる