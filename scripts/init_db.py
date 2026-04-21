#!/usr/bin/env python3
"""B2B 销售智能助理 v5.0 - 数据库初始化脚本"""

import sqlite3
import os

DB_DIR = os.path.expanduser("~/.qoderwork/data/Sloth-Sales-Eido")
DB_PATH = os.path.join(DB_DIR, "sales_crm.db")


def init_database():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 客户信息表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        market TEXT,
        industry TEXT,
        qualification_tags TEXT DEFAULT '{}',
        company_type TEXT,
        employee_count_range TEXT,
        revenue_last_3_years TEXT DEFAULT '[]',
        financial_status TEXT DEFAULT '未知',
        procurement_category TEXT,
        current_solution TEXT DEFAULT '{}',
        key_contacts TEXT DEFAULT '[]',
        decision_chain TEXT DEFAULT '[]',
        competitor_intelligence TEXT DEFAULT '[]',
        data_source TEXT,
        monitor_flag INTEGER DEFAULT 0,
        created_at TEXT DEFAULT (datetime('now', 'localtime')),
        updated_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
    """)

    # 销售漏斗表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_funnel (
        funnel_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        current_stage TEXT DEFAULT '线索',
        is_stalled INTEGER DEFAULT 0,
        stalled_since TEXT,
        stage_history TEXT DEFAULT '[]',
        probability INTEGER DEFAULT 10,
        estimated_deal_value REAL DEFAULT 0,
        deal_currency TEXT DEFAULT 'CNY',
        payment_terms TEXT,
        next_action TEXT,
        next_contact_date TEXT,
        key_date TEXT DEFAULT '[]',
        priority TEXT DEFAULT '中',
        owner TEXT DEFAULT '当前用户',
        health_score INTEGER DEFAULT 70,
        stuck_reason TEXT,
        created_at TEXT DEFAULT (datetime('now', 'localtime')),
        updated_at TEXT DEFAULT (datetime('now', 'localtime')),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
    """)

    # 跟进记录表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_log (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        activity_type TEXT,
        relationship_investment_type TEXT,
        target_contact TEXT,
        timestamp TEXT DEFAULT (datetime('now', 'localtime')),
        summary TEXT,
        result TEXT,
        relationship_score INTEGER,
        next_stage_suggestion TEXT,
        tags TEXT,
        key_extracted_info TEXT DEFAULT '{}',
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
    """)

    # 案例库表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS case_library (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT DEFAULT '成功',
        industry TEXT,
        scale TEXT,
        procurement_category TEXT,
        original_solution TEXT,
        pain_point TEXT,
        solution TEXT,
        quantifiable_benefit TEXT,
        customer_quote TEXT,
        lost_to TEXT,
        lesson_learned TEXT
    )
    """)

    # 用户偏好表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_preferences (
        pref_key TEXT PRIMARY KEY,
        pref_value TEXT
    )
    """)

    conn.commit()
    conn.close()

    print(f"[v5.0] 数据库初始化完成: {DB_PATH}")
    print("=" * 50)
    print("表结构:")
    print("  - customers        客户信息表 (20 cols)")
    print("  - sales_funnel     销售漏斗表 (19 cols)")
    print("  - activity_log     跟进记录表 (12 cols)")
    print("  - case_library     案例库表   (12 cols)")
    print("  - user_preferences 用户偏好表 (2 cols)")
    print("=" * 50)
    print("v5.0 关系驱动·教练增强版")
    print("新增: 阶段回退/Stalled、竞品情报、关系投资、")
    print("      失败案例、多币种、东南亚适配等")


if __name__ == "__main__":
    init_database()
