'''
Checkpoint 1: Python Review
CSE 111-07
Nicholas Wilkins
01/10/2024

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your hearts maximum rate.
'''

user_age = int(input('\nPlease enter your age as a whole number: '))
maximum_heart_rate = 220 - user_age
heart_rate_range_high = maximum_heart_rate * 0.85
heart_rate_range_low = maximum_heart_rate * 0.65

print(f'\nWhen you exercise to strengthen your heart, you should keep your heart rate between {heart_rate_range_high:.0f} and {heart_rate_range_low:.0f} beats per minute.\n')