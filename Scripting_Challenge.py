



import sys
from dateutil.parser import parse
from statistics import mean
import re

try:#check if both input and output filenames are supplied
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
except IndexError:
        print("missing input/output file names")  
        sys.exit(0)
        


try: # handles missing input arguments or file not found exceptions
    
    with open(inputFileName,'r') as infile, open(outputFileName,'w') as outfile :
        next(infile) #skipping the header line
        outfile.write("Order_id" + "\t" + "Order_date" + "\t" + "User_id" + "\t" + "Avg_item_price" + "\t" + "Start_page_url" + "\t" + "Error_msg" +"\n")
        
        for line in infile: # read each line from the file
            order_id,order_date,user_id,avg_item_price,start_page_url,error_msg='','','','','',''
            row=line.split("\t")
            orderDate=re.split('[:]+',row[0]) #eliminating any continuos delimiters like (::)
            if orderDate[0] and orderDate[1]: #check if order number or date is available
                try: #check if Order Number is valid
                    order_id=int(orderDate[0])
                except ValueError:
                    error_msg="Invalid Order Number,"
                    
                try: #check if Order Date is a valid date
                     order_date=parse(orderDate[1][0:4]+'-'+orderDate[1][4:6]+'-'+orderDate[1][6:8]).date() #check if date is valid
                except ValueError:
                     error_msg+="Invalid Date,"
            else:
                error_msg+="Missing Order Number and/or Date,"
            
            if row[1]: #check if User Id is a valid number
                try:
                    user_id=int(row[1])
                except ValueError:
                    error_msg+="Invalid User Id,"
            else:
                error_msg+="Missing UserId,"
            
            try: #check if all the prices are valid
                price_list=[float(x) for x in row[2:6] if x!='0' and x!=''] #exclude prices which are either zero or blank
                if price_list: #exclude rows where all the item prices are zero or blank
                    avg_item_price=round(mean(price_list),2)
                else: 
                    error_msg+="Zero item price,"    
                    
            except ValueError:
                error_msg+="Invalid Item Price,"
            if row[6]=='' or not row[6].startswith("http://www.insacart.com"): 
                error_msg+="Invalid URL," 
            else:   
                start_page_url=row[6].strip()
                
            #print (order_id,order_date,user_id,avg_item_price,start_page_url,error_msg[:-1])    
            outfile.write(str(order_id) + "\t" + str(order_date) + "\t" + str(user_id) + "\t" + str(avg_item_price) + "\t" + start_page_url + "\t" + error_msg[:-1] +"\n")
        
except FileNotFoundError:
        print("Wrong file or file path")           
except IndexError:
        print("Invalid number of columns")    
except:
        print("File parsing failed")
        