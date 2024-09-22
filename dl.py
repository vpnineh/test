import urllib.request 
urllib.request.urlretrieve("https://raw.githubusercontent.com/Surfboardv2ray/Subs/refs/heads/main/IPTest/ips.txt", "ips.txt")
# Open the source text files
file1 = open('ips.txt', 'r')
file2 = open('bestips.txt', 'r')


# Read the contents of the text files
content1 = file1.read()
content2 = file2.read()


# Close the source text files
file1.close()
file2.close()


# Open the destination file
destination_file = open('ips.txt', 'w')

# Write the concatenated content to the destination file
destination_file.write(content1 + content2)
# Close the destination file
destination_file.close()
