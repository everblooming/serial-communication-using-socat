# install socat
```shell
sudo apt install socat
socat -V
```

# 仮想シリアルポート作成
```
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

## 構文
`socat [options] <address> <address>`

## options
振る舞いやアドレス仕様を決める引数。
-dの数で表示されるメッセージ領域を決定する。

## PTY
疑似端末のこと。
仮想コンソール、端末装置、シリアルポートハードウェアなどを私用しないテキスト端末インターフェースを提供する。

## raw
raw modeに設定。
無処理でのデータの受け渡しを行う。
現在はrawerまたはcfmakerawのオプションを推奨。

## rawer
raw modeを設定し、echoをオフに設定。

## cfmakeraw
raw modeを設定し、echoをオフに設定。
termios.hのcfmakeraw()を呼び出すか、この呼び出しをシミュレート

# pythonで送受信テスト

## install packages
```
pip install pyserial pytz
```

## ポートの指定
`tx.py`や`rx.py`の`port_name`の`XX`をsocatで生成された仮想ポートに書き換える。

```python
# open port
port_name = '/dev/pts/XX'
```

## 実行
```
python rx.py
python tx.py
```

# references
- [socatで仮想シリアルポートを作る](https://qiita.com/uhey22e/items/dc41d7fa1075970e66a1)
- [pySerial-shortintro](https://pyserial.readthedocs.io/en/latest/shortintro.html)
- [socat を使う (シリアル-TCP変換, etc.)](https://ma-tech.centurysys.jp/doku.php?id=mae3xx_tips:use_socat:start)
- [コマンド socat ソケットリレーツール (proxy)](http://x68000.q-e-d.net/~68user/unix/pickup?socat)
- [official socat doc](http://www.dest-unreach.org/socat/doc/socat.html#EXAMPLE_OPTION_TERMIOS_RAWER)
- [Getting started with socat, a multipurpose relay tool for Linux](https://www.redhat.com/sysadmin/getting-started-socat)