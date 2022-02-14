# 1 - Describe what this script does part by part

# This creates a dataframe object which is then stored into variable df1. This data frame then gets 3 columns full of values 'combined' to it using the c() function:
# First a name column, then a State column, then the Sales column
# This organizes the data in a simple tabular format for easy displaying

df1=data.frame(Name=c('James','Paul','Richards','Marico','Samantha','Ravi','Raghu',
                      'Richards','George','Ema','Samantha','Catherine'),
               State=c('Alaska','California','Texas','North Carolina','California','Texas',
                       'Alaska','Texas','North Carolina','Alaska','California','Texas'),
               Sales=c(14,24,31,12,13,7,9,31,18,16,18,14))

# Here the aggregate() function is called, which will display stats for the input (the df1 dataframe in this case)
# df1$Sales: specifies that aggregate() should pull stats on the Sales column in the df1 dataframe
# by=list(df1$State): the by param specifies what to group the output by, in this case group by States in df1
# FUN=sum: FUN denotes a function to be ran on the data set, in this case the sum() function to just sum the values
# All of these combined, it outputs the total sales per state stored in df1
aggregate(df1$Sales, by=list(df1$State), FUN=sum)

# library() will import a library to use, in this case dplyr for extra data manipulation capabilities.
library(dplyr)

# With dplyr now installed, this grants access to the %>% operator, and the group_by() and summarise() functions.
# %>% acts as a 'pipe' moving the left input's data into the right input. So df1's values gets passed to group_by(), which
# dplyr 'primes' the data to be grouped by State that is then piped to summarise() to output sum_sules. sum_sales is the result of sum(Sales), which just
# is the sum of the Sales column per state because of the previous group_by()

# df1 is then output, showing the total sales per state.

df1 %>% group_by(State) %>% summarise(sum_sales = sum(Sales))


# ~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~


# Question 2
df2 = read.csv("/Users/skyler/Downloads/CSC302 DATA/WorldCupMatches.csv", header=TRUE, sep = ",")

# 2a: Size of data frame (row, columns)
dim(df2)

# 2b: Use summary function to report statistical summary of the data
summary(df2)

# 2c: Total unique locations Olympics was held at
count(unique(df2[c("City")]))

# 2d: Find average attendance
mean(df2$Attendance, na.rm=TRUE)

# 2e: For each home team, how many goals were scored
aggregate(df2$Home.Team.Goals, by=list(df2$Home.Team.Name), FUN=sum)

# 2f: What is the average number of attendees for each year? Is there a trend or pattern in the data in that sense?
aggregate(df2$Attendance, by=list(df2$Year), FUN=mean)
# There does not appear to be a trend besides certain years it spikes and then the next 2-4 years are low until another spike happens


# ~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~


# Question 3
df3 = read.csv("/Users/skyler/Downloads/CSC302 DATA/metabolite.csv", header=TRUE, sep = ",")


# 3a) Find how many Alzheimer's patients there are in the data set
sum(df3$Label=="Alzheimer")

# 3b) Determine the number of missing values for each column
colSums(is.na(df3))

# 3c) Remove the rows which have a missing value for the Dopamine column, and assign the result to a new data frame
df3c <- na.omit(df3$Dopamine)

# 3d) In the new data frame, replace the missing values in the c4-OH-Pro column with the median value of the same column. 
df3$c4.OH.Pro[is.na(df3$c4.OH.Pro)] <- median(df3$c4.OH.Pro, na.rm = TRUE)
df3c <- df3$c4.OH.Pro
df3c