# 2021年度ロボットシステム学：課題2「count.py・twice.py」

## 目的
・Ubuntu18.04にRaspberry Pi 3 を使用し、任意の数字を操作し、標準出力する事を目的とする。

## 動作環境
・Ubuntu18.04（OS）

## 使用する物
・Raspberry Pi　3　×1

## 実行操作
1．Ubuntu18.04を立ち上げる

2．Raspberry Pi 3 に電源を入れ、Ubuntu18.04に接続する

3．roscoreを立ち上げる

### ノード1の作成
1．vi count.py と打ち込み、ノード1を作る

2．vi count.py にプログラムを書き込む

3．:wqでファイルを保存する

4．chmod +x count.py と打ち込み、ファイルを実行できるようにパーミッション設定を行う

5．rosrun mypkg count.py と打ち込み、ファイルを実行する（成功すると、何も返ってこない）

6．違うコマンドでrosnode list と rostopic listと打ち込み、ノードとトピックの確認を行う

7．rostopic echo /count_up で実行する（成功すると、+1された数字が標準出力される）

### ノード2の作成
1．vi twice.py と打ち込み、ノード2を作成する

2．:wqでファイルを保存する

3．rosrun mypkg twice.py と打ち込み、ファイルを実行する（成功すると、「INFO」～ +2された数字が標準出力される）

### ノード3の作成
1．vi twice.py と打ち込み、ノード2を書き換える

2．:wqでファイルを保存する

3．rosrun mypkg twice.py と打ち込み、ファイルを実行する（成功すると、何も返ってこない）

4．違うコマンドでrosnode list と rostopic listと打ち込み、ノードとトピックの確認を行う

5．rostopic echo /twice.py で実行する（成功すると、+2された数字が標準出力される）

##   ライセンス
・BSD3-Clause "New" or "Revised" License

## 動作
・youtubeにて、その動作を確認できる動画を公開する

・URL→https://youtu.be/NOSOB0cSlz8
