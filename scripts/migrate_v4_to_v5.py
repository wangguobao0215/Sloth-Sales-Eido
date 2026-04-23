#!/usr/bin/env python3
"""深耕 · 销售管理 - v4.0 → v5.0 数据库迁移脚本

对已有数据库执行 ALTER TABLE 补齐 v5.0 新增字段。
安全设计：
- 逐列检测，已有则跳过
- 不删除任何数据
- 迁移前自动备份
"""

import sqlite3
import os
import shutil
from datetime import datetime

DB_DIR = os.path.expanduser("~/.qoderwork/data/Sloth-Sales-Eido")
DB_PATH = os.path.join(DB_DIR, "sales_crm.db")

# v5.0 新增字段定义: (table, column, type_with_default)
V5_NEW_COLUMNS = [
    # customers 表新增 4 列
    ("customers", "country", "TEXT"),
    ("customers", "market", "TEXT"),
    ("customers", "company_type", "TEXT"),
    ("customers", "competitor_intelligence", "TEXT DEFAULT '[]'"),

    # sales_funnel 表新增 5 列
    ("sales_funnel", "is_stalled", "INTEGER DEFAULT 0"),
    ("sales_funnel", "stalled_since", "TEXT"),
    ("sales_funnel", "stage_history", "TEXT DEFAULT '[]'"),
    ("sales_funnel", "deal_currency", "TEXT DEFAULT 'CNY'"),
    ("sales_funnel", "payment_terms", "TEXT"),

    # activity_log 表新增 2 列
    ("activity_log", "relationship_investment_type", "TEXT"),
    ("activity_log", "target_contact", "TEXT"),

    # case_library 表新增 3 列
    ("case_library", "case_type", "TEXT DEFAULT '成功'"),
    ("case_library", "lost_to", "TEXT"),
    ("case_library", "lesson_learned", "TEXT"),
]


def get_existing_columns(cursor, table):
    """获取表的现有列名集合"""
    cursor.execute(f"PRAGMA table_info({table})")
    return {row[1] for row in cursor.fetchall()}


def migrate():
    if not os.path.exists(DB_PATH):
        print(f"[迁移] 数据库不存在: {DB_PATH}")
        print("[迁移] 请先运行 init_db.py 创建新库（已包含 v5.0 字段）")
        return

    # 1. 备份
    backup_name = f"sales_crm_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
    backup_path = os.path.join(DB_DIR, backup_name)
    shutil.copy2(DB_PATH, backup_path)
    print(f"[迁移] 备份完成: {backup_name}")

    # 2. 连接并逐列迁移
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    added = 0
    skipped = 0

    for table, column, col_def in V5_NEW_COLUMNS:
        existing = get_existing_columns(cursor, table)
        if column in existing:
            skipped += 1
            continue

        sql = f"ALTER TABLE {table} ADD COLUMN {column} {col_def}"
        try:
            cursor.execute(sql)
            added += 1
            print(f"  [+] {table}.{column} — 已添加")
        except Exception as e:
            print(f"  [!] {table}.{column} — 失败: {e}")

    conn.commit()

    # 3. 验证
    print(f"\n[迁移] 完成: 新增 {added} 列, 跳过 {skipped} 列（已存在）")
    print("[迁移] 验证各表列数:")
    for table in ["customers", "sales_funnel", "activity_log", "case_library"]:
        cols = get_existing_columns(cursor, table)
        print(f"  {table}: {len(cols)} 列")

    conn.close()
    print(f"\n[迁移] v4.0 → v5.0 迁移完成！备份文件: {backup_path}")


if __name__ == "__main__":
    migrate()
