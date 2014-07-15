
csv_data <-list.files(pattern='*.csv')
wc_preds <- c()

for(i in 1:length(csv_data)){
	temp_df <- read.csv(csv_data[i])
	temp_df['date'] = paste(substring(csv_data[i],8,9), substring(csv_data[i],10,11), substring(csv_data[i],4,7), sep="-")
	temp_df['time'] = paste(substring(csv_data[i],13,14), substring(csv_data[i],15,16), substring(csv_data[i], 17,18), sep=":")
	# temp_df["date_time"] <- as.POSIXlt(strptime(substring(csv_data[i],4,18), "%Y%m%d-%H%M%s"))
	# assign(paste("wc_preds",i,sep=""), temp_df)
	
	wc_preds <- c(wc_preds, temp_df)
}