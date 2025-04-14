# Objective 3: Scatter Plot – Dried Up vs. Destroyed Sources
plt.figure(figsize=(8, 6))
plt.scatter(df['Dried up - No.'], df['Destroyed beyond repair - No.'], alpha=0.5)
plt.title('Scatter Plot: Dried Up vs. Destroyed Sources')
plt.xlabel('Dried up - No.')
plt.ylabel('Destroyed beyond repair - No.')
plt.grid(True)
plt.tight_layout()
plt.show()
