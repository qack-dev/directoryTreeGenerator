# Directory Tree Generator

`Directory Tree Generator`は、指定されたディレクトリの階層構造を分かりやすいツリー形式でコンソールに出力する、シンプルなコマンドラインツールです。

このツールは、Pythonのハンズオントレーニングの一環として開発されました。Pythonの基本的なファイルシステム操作（`os`モジュール）と再帰関数の使い方を学ぶプロジェクトです。

## 主な特徴

-   **直感的なツリー表示**: ディレクトリ構造を視覚的に素早く把握できます。
-   **コマンドライン操作**: ターミナルやコマンドプロンプトから手軽に実行可能です。
-   **依存関係なし**: Pythonの標準ライブラリのみで動作するため、追加のインストールは不要です。

## 実行例

以下は、`Y:\music\Bohemianvoodoo` ディレクトリに対してツールを実行した際の出力例です。

![コマンド実行例](https://github.com/qack-dev/directoryTreeGenerator/execution_example.png)

## 使い方

### 前提条件

-   Python 3.x がインストールされていること。

### 1. リポジトリのクローン

まず、このリポジトリをローカルマシンにクローンします。

```bash
git clone https://github.com/qack-dev/directoryTreeGenerator.git
cd directoryTreeGenerator
```

### 2. スクリプトの実行

以下のコマンドを実行して、ディレクトリツリーを生成します。
`[directory_path]` の部分を、構造を表示したいディレクトリのフルパスに置き換えてください。

```bash
python -B main.py [directory_path]
```

**コマンド例:**

-   **Windowsの場合:**
    ```bash
    python -B main.py "C:\Users\YourUser\Documents"
    ```

-   **macOS / Linuxの場合:**
    ```bash
    python -B main.py /home/youruser/documents
    ```

## コードの簡単な解説

このツールの中心的な機能は、`main.py` 内の `print_tree` 関数によって実現されています。

この関数は「再帰」というテクニックを使用しています。ディレクトリを探索中に新しいサブディレクトリを見つけると、そのサブディレクトリを対象として自分自身を再度呼び出します。これにより、どれだけ深い階層のディレクトリ構造であっても、すべてを正確に表示することができます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
