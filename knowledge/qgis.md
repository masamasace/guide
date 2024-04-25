---
title: "QGISの使い方"
date: "2024-04-15"
---

QGISの使い方についてまとめたページです．内容については系統立って整理されておらず雑多です．

## 粗いメッシュベクターデータから密な点群ベクターデータを作成する方法

1. CRS(座標参照系)を変更する
    - レイヤのプロパティを開く
    - `座標参照系`を選択し，直行直角座標系に変更する
1. 重心(Centorid)を求める
    - プロセッシングツールボックスを開く
    - `Centroid`を検索し，選択します
    - 入力レイヤを選択します
    - 出力ファイル名を指定します
    - `Run`をクリックします
1. IDW(逆距離加重法)を適用する
    - プロセッシングツールボックスを開く
    - `IDW`を検索し，`Grid (IDW with nearest neighbor searching)`を選択します
    - 入力レイヤを選択します
    - `Smoothing`を適切な値に変更する
        - このとき`CRS`が直行直角座標系であると単位が`m`になり結果が想像しやすくなる
    - `The radisu of the search circle`を重心距離の最大値に設定する
    - `Maximum number of data points to use`を重心点数にする
    - `Z value from field`を適切なフィールドに設定する
    - `Additional command-line parameters`に以下の値を入力する
        - `-txe`と`-tye`を: 点が欲しい範囲を指定したCRSで
        - `-tr`を適切な値に設定する: 縦方向と横方向の解像度を指定する
    - 出力ファイル名を指定します
    - `Run`をクリックします
1. ここから手順が2つに分かれます．
    1. 方法1
        1. `Regular points`を作成する
            - プロセッシングツールボックスを開く
            - `Regular points`を検索し，選択します
            - `Input Extent`を適切な値に変更する
            - `Point spacing / count`を適切な値に変更する
                - ここでの値は`IDW`の`-tr`と同じ値かそれよりも大きい値にしましょう
            - `Initial inset from corner`を適切な値に変更する
            - 出力ファイル名を指定します
            - `Run`をクリックします
        1. `Sample raster vlues`を実行する
            - プロセッシングツールボックスを開く
            - `Sample raster values`を検索し，選択します
            - `Input layer`に`Regular points`の出力ファイルを指定します
            - `Raster layer`に`IDW`の出力ファイルを指定します
            - 出力ファイル名を指定します
            - `Run`をクリックします
    1. 方法2
        1. `Raster pixels to points`を実行する
            - プロセッシングツールボックスを開く
            - `Raster pixels to points`を検索し，選択します
            - `Input layer`に`IDW`の出力ファイルを指定します
            - 出力ファイル名を指定します
            - `Run`をクリックします


## QGISのバージョン3以上でSAGAを使用する方法

QGISのバージョン3以上でSAGAを使用する方法について説明します．
1. プラグインをインストールする
    - プラグイン > 管理とインストール > プラグインをインストールする
    - `Processing Saga NextGen Provider`プラグインをインストールする
    - ここに利用可能なSAGAのバージョンが書かれているのでそのバージョンをメモする
        - 現時点(2024年4月15日)では，`SAGA`のバージョンは9.1，`Processing Saga NextGen Provider`のバージョンは1.0.0でした
    - 一旦QGISを終了させます．

1. SAGAのインストール
    - [SAGAのホームページ](https://saga-gis.sourceforge.io/en/index.html)
    - ダウンロード > `SAGA - 9` > `SAGA - 9.1.0` > `saga-9.1.0_x64.zip`をダウンロードする
        - 上記はWindowsの場合の例です．他のOSの場合は適宜ダウンロードしてください
    - ダウンロードしたファイルを解凍します
    - 解答してできたフォルダごと`C:\Program Files\QGIS 3.28.5\apps\saga`に移します．
        - ここで，`3.28.5`はQGISのバージョンによって異なります．適宜変更してください．
        - また，既存のSAGAを残しておきたい場合には，`C:\Program Files\QGIS 3.28.5\apps\`の中に`saga-9.1.0`などのフォルダを作成し，その中に移動させてください．
    - `C:\Program Files\QGIS 3.28.5\apps\saga`あるいは自分が作成したフォルダの中に`saga_cmd.exe`があることを確認します．

1. QGIS内での設定
    - QGISを開きます
    - プロセッシングツールボックスを開きます
    - スパナ(🔧)のアイコンをクリックします．
    - `Options -- Processing`の画面が開かれるので，`Providers`タブを選択します．
    - `SAGANG`の項目にカーソルを合わせ，先ほど作成したフォルダを選択するか，フォルダパスを直接入力します．
    - `Enable SAGA Import/Export optimizations`にチェックを入れます．
        - なぜこうするかはわかりません
    - `OK`をクリックします．
    - QGISを再起動します．

1. (補足)`Ordinary Krigging`について
    - 今回，`Ordinary Krigging`を使用する際に，以下のようなトラブルシュートを行いました
        - 用いるデータは，あらかじめ`shp`ファイルに変換しておく必要がありました
            - `geopackage`ファイルだとだめみたい？
        - またCRSは直行直角座標系に変換しておく必要がありました
            - 単位が緯度経度だとだめみたい？
        



### 参考リンク

- [QGIS in Mineral Exploration &#124; 14.5. Installing the SAGA Next Gen Provide](https://qgis-in-mineral-exploration.readthedocs.io/en/latest/source/how_to/add_saga_next_gen.html)
- [Installing the "SAGA Next Gen" plugin in QGIS](https://www.youtube.com/watch?v=VKdaripCups)

## フィールド計算機で，ある属性フィールドを別の属性フィールドの値によって指定して，新しい属性フィールドを作成する方法
1. レイヤのプロパティを開く
    - レイヤのプロパティを開くには，レイヤの右クリック > プロパティを選択します．
    - あるいは，レイヤのプロパティアイコンをクリックします．
1. フィールド計算機を開く
    - レイヤのプロパティウインドウの中にあるフィールドを選択します．
    - フィールド計算機アイコンをクリックします．
1. 新しいフィールドを作成する
    - 新しいフィールドを作成するには，新しいフィールドを追加します．
    - 新しいフィールドの名前を入力します．
    - 新しいフィールドの型を選択します．
    - `attribute( concat('Peak',  "Exported Time-series (Butterworth-Sectioned)" ))`のような式を入力します．
        - この式は，"Exported Time-series (Butterworth-Sectioned)"というフィールドの値を取得し，その前に"Peak"という文字列を追加します．
        - さらにこの文字列が参照したいフィールド名となっており，最終的にそのフィールドの値を新しいフィールドに追加します．
        
## Excelファイルの読み込み方法

QGISでExcelファイルを読み込む方法について説明します．エクセルファイルには最低限，緯度，経度，地物名の情報が含まれていると仮定します．

1. エクセルデータをドラックアンドドロップでQGISに読み込む
    - 読み込みが完了すると，テーブルのアイコンがレイヤのウインドウの中に表示されます
    - キャンバスの中には何も表示されません
1. プロセシングツールボックスを開く
    - プラグイン > プロセシング > ツールボックスを選択します
    - 検索欄に`table`と入力します
    - `Table to point`，日本語であれば`テーブルから点レイヤを作成`を選択します
    - X値には経度(long)，Y値には緯度(lat)を選択します
    - 出力ファイル名を指定します．(そのままであれば，一時レイヤが生成されます)
    - `Run`あるいは`実行`をクリックします

## Openstreetmapで特定の地物だけを表示する方法

OpenStreetMapから特定の地物だけを表示する方法について説明します．具体的な手順は以下のとおりです．今回は建物データに限った場合を例に説明します．

1. OpenStreetMapから建物データを取得

まず、OpenStreetMapから建物データを取得する必要があります．これを行う方法はいくつかありますが、一般的な方法の1つは、Overpass APIを使用することです．Overpass APIを使用してOSMから特定のデータをクエリすることができます．QGISのQuickOSMプラグインを使用して簡単に行う方法を以下に示します．

- QuickOSMプラグインをインストールします
    - QGISを開き、Plugins > Manage and Install Plugins...に移動します．"QuickOSM"を検索してインストールします．
- QuickOSMを開きます
    - Vector > QuickOSM > QuickOSM...に移動します．
- 建物をクエリします
    - "Key"フィールドにbuildingと入力します．
    - "Value"フィールドは空のままにしておくか、必要に応じて建物の種類を指定します．
        - 例えば，住宅のみを取得したい場合はhouseあるいはapartmentsなどを指定します．
    - 建物を取得したいエリアを選択します．複数の選択方法があり，座標を入力するか，地図から選択するか，レイヤ境界から選択するなどの方法があります．
- `Run Query`をクリックします．これにより、建物データがダウンロードされ、QGISプロジェクトにロードされます．
