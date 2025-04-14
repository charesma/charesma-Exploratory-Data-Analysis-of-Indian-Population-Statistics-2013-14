# Objective 5: Histogram – Distribution of Dried Up Sources 
plt.figure(figsize=(8, 6))
plt.hist(df['Dried up - No.'], bins=20, color='orange', edgecolor='black')
plt.title('Histogram: Distribution of Dried Up Sources Across Villages')
plt.xlabel('Number of Dried Up Sources')
plt.ylabel('Number of Villages')
plt.tight_layout()
plt.show()
