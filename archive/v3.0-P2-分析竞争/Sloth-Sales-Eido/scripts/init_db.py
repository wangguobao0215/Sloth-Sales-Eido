#!/usr/bin/env python3
"""B2B 销售智能助理 v3.0 - 数据库初始化脚本"""

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
        industry TEXT,
        qualification_tags TEXT DEFAULT '{}',
        employee_count_range TEXT,
        revenue_last_3_years TEXT DEFAULT '[]',
        financial_status TEXT DEFAULT '未知',
        procurement_category TEXT,
        current_solution TEXT DEFAULT '{}',
        key_contacts TEXT DEFAULT '[]',
        decision_chain TEXT DEFAULT '[]',
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
        probability INTEGER DEFAULT 10,
        estimated_deal_value REAL DEFAULT 0,
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

    # 案例库表 [v3.0 新增]
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS case_library (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,
        industry TEXT,
        scale TEXT,
        procurement_category TEXT,
        original_solution TEXT,
        pain_point TEXT,
        solution TEXT,
        quantifiable_benefit TEXT,
        customer_quote TEXT
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
    print(f"[v3.0] 数据库初始化完成: {DB_PATH}")
    print("表结构: customers, sales_funnel, activity_log, case_library, user_preferences")
    print("v3.0 新增: case_library 案例库表")
    print("v3.0 新增能力: 健康度评分、阻力点诊断、竞品话术、业绩仪表盘、协作快照、角色化沟通")


if __name__ == "__main__":
    init_database()
