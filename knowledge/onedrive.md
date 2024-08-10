## やりたいこと
- Onedriveの共有リンクをコマンドラインから取得、削除したい

## ひっかかった場所
- Powershellのバージョンは7以上じゃないといけない。
    - 自分の環境では5.1だったので、アップデートが必要

## 2024/07/15 調査
- Powershellのv7をインストール
    - コマンドプロンプトから`winget install --id=Microsoft.PowerShell`を実行
    - `winget`はWindows Package Managerのこと
- ターミナルというアプリを起動
    - なければMicrosoft Storeからインストール
- ターミナルのシェルに`PowerShell 7`追加
    - 設定>一番左の下`新しいプロファイルを追加します`>名前とコマンドラインを指定
    - 自分の環境では`"C:\Program Files\PowerShell\7\pwsh.exe`に存在
- `Install-Module PnP.PowerShell　-force`を実行
- `Connect-PnPOnline -Url "<サイトURL>" -UseWebLogin`を実行
    - URLはOnedriveの共有リンクを取得したいフォルダのURLの先頭部分(`personal/`の次の部分まで)
    - ブラウザが開いてログインを求められる
- `Get-PnPSite`を実行
- 認証情報が足りなくてだめ