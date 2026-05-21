import pandas as pd
import os

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv('data/students.csv')

# ── Calculations ───────────────────────────────────────
avg_hours       = df['total_hours_studied'].mean()
rank1_student   = df[df['rank'] == 1].iloc[0]
rank2_student   = df[df['rank'] == 2].iloc[0]
rank3_student   = df[df['rank'] == 3].iloc[0]
last_student    = df[df['rank'] == df['rank'].max()].iloc[0]

# ── Build Report ───────────────────────────────────────
report = f"""
╔══════════════════════════════════════════════╗
       STUDENT STUDY HOURS ANALYSIS REPORT     
╚══════════════════════════════════════════════╝

📊 OVERALL AVERAGE
──────────────────────────────────────────────
  Average Hours Studied by All Students : {avg_hours:.2f} hrs/year

🏆 TOP RANKED STUDENTS
──────────────────────────────────────────────
  🥇 Rank 1 : {rank1_student['name']:<12} → {rank1_student['total_hours_studied']} hrs/year
  🥈 Rank 2 : {rank2_student['name']:<12} → {rank2_student['total_hours_studied']} hrs/year
  🥉 Rank 3 : {rank3_student['name']:<12} → {rank3_student['total_hours_studied']} hrs/year

📉 LAST RANKED STUDENT
──────────────────────────────────────────────
  🔴 Rank {int(last_student['rank'])} : {last_student['name']:<12} → {last_student['total_hours_studied']} hrs/year

💡 INSIGHTS
──────────────────────────────────────────────
  Hours above average : {rank1_student['total_hours_studied'] - avg_hours:.2f} hrs  (Rank 1 vs Avg)
  Hours below average : {avg_hours - last_student['total_hours_studied']:.2f} hrs  (Avg vs Last)
  Gap (Rank 1 vs Last): {rank1_student['total_hours_studied'] - last_student['total_hours_studied']} hrs

══════════════════════════════════════════════
"""

# ── Print to Console ───────────────────────────────────
print(report)

# ── Save to File ───────────────────────────────────────
os.makedirs('output', exist_ok=True)
with open('output/results.txt', 'w') as f:
    f.write(report)

print("✅ Results saved to output/results.txt")