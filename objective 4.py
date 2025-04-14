# Objective 4: Horizontal Bar Chart – Issues by Cause in Anantapur District


district_data = df[df['District'].str.upper() == 'ANANTAPUR']
causes = ['Salinity - No.', 'Dried up - No.', 'Destroyed beyond repair - No.',
          'Sea water intrusion  - No.', 'Industrial effluents - No.', 'Other reasons - No.']
cause_totals = district_data[causes].sum()

plt.figure(figsize=(9, 6))
plt.barh(causes, cause_totals, color='mediumseagreen')
plt.xlabel('Number of Issues')
plt.title('Horizontal Bar Chart: Issues by Cause in Anantapur District')
plt.tight_layout()
plt.show()
