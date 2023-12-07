import pandas as pd

# Veri kümelerinin URL'lerini tanımla
base_url = "../data/covid/"
infected_dataset_url = base_url + "time_series_covid19_confirmed_global.csv"
recovered_dataset_url = base_url + "time_series_covid19_recovered_global.csv"
deaths_dataset_url = base_url + "time_series_covid19_deaths_global.csv"

# Veri kümelerini pandas DataFrame'leri olarak oku
infected_df = pd.read_csv(infected_dataset_url)
recovered_df = pd.read_csv(recovered_dataset_url)
deaths_df = pd.read_csv(deaths_dataset_url)

# Ülke bazında toplam vaka, iyileşme ve ölüm sayılarını hesapla
total_infected = infected_df.groupby('Country/Region').sum().iloc[:, -1]
total_recovered = recovered_df.groupby('Country/Region').sum().iloc[:, -1]
total_deaths = deaths_df.groupby('Country/Region').sum().iloc[:, -1]

# Toplam vaka, iyileşme ve ölüm sayılarını içeren bir DataFrame oluştur
summary_df = pd.DataFrame({
    'Toplam Vaka Sayısı': total_infected,
    'Toplam İyileşme Sayısı': total_recovered,
    'Toplam Ölüm Sayısı': total_deaths
})

# Toplam vaka sayısına göre sırala
summary_df = summary_df.sort_values(by='Toplam Vaka Sayısı', ascending=False)

# En çok vaka görülen ilk 10 ülkeyi göster
print("\nToplam Vaka Sayısına Göre İlk 10 Ülke:")
print(summary_df.head(10))