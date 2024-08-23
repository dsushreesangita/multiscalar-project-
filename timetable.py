import pandas as pd
import numpy as np

file_path = 'data2.xlsx'
df = pd.read_excel(file_path)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6
timetable = pd.DataFrame(index=range(1, periods_per_day + 1), columns=days)

subject_allocation = {subject: 0 for subject in df['Subject']}

df = df.sort_values(by='Priority')


def assign_subject(timetable, df, subject_allocation):
    for _, row in df.iterrows():
        subject = row['Subject']
        teacher = row['Teacher']
        periods_required = row['Number of classes per week']
        assigned_periods = subject_allocation[subject]

        for day in timetable.columns:
            for period in timetable.index:
                if pd.isna(timetable.loc[period, day]) and assigned_periods < periods_required:
                    timetable.loc[period, day] = f"{subject} ({teacher})"
                    assigned_periods += 1
                    subject_allocation[subject] = assigned_periods
                if assigned_periods == periods_required:
                    break
            if assigned_periods == periods_required:
                break


assign_subject(timetable, df, subject_allocation)

output_file_path = 'table.xlsx'
timetable.to_excel(output_file_path)

print("Generated" + output_file_path)