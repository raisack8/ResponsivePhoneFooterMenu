from django.db import models

"""
[makemigrations]コマンドはデータベースの設計図の変更を反映させる。
モデルの構造を変更したときに、上記コマンドを実行すると、
「今DBにそのカラムないけどどうする？」とか聞かれるらしい。

一方[migrate]コマンドはDBへの変更を反映するもの。
"""
