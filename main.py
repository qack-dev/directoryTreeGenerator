#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# ディレクトリパスとインデントレベルを引数に取る関数
def print_tree(path, level):
    # 指定したディレクトリに含まれるファイルやディレクトリの一覧をリストとして取得する。
    entries = os.listdir(path)
    # リストをループ
    for entry in entries:
        # 表示
        if level == 0:
            print(f'* {entry}')
        else:
            indent = '\t' * level
            print(f'{indent}↳ * {entry}')
        # フルパス
        full_path = os.path.join(path,entry)
        # もしディレクトリなら
        if os.path.isdir(full_path):
            # 再帰的に呼び出す
            print_tree(full_path, level + 1)

# メイン関数
def main():
    # 文字列リテラルの前に r を付けると、その文字列は「RAW文字列」となり、バックスラッシュは単なる文字として扱われる。
    # args = ["", r"Y:\music\ゲーム"]
    args = sys.argv # リスト
    print_tree(args[1], 0)

if __name__ == "__main__":
    main()
