# Objective 2: Bar Chart – Total Water Source Issues by State

plt.figure(figsize=(12, 6))
plt.bar(state_issues.index, state_issues.values, color='skyblue')
plt.xticks(rotation=90)
plt.title('Bar Chart: Water Source Issues by State')
plt.xlabel('State')
plt.ylabel('Total Issues')
plt.tight_layout()
plt.show()
