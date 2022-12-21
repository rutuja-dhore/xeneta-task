from urllib import response
import psycopg2
import psycopg2.extras
from flask import Flask,request
from datetime import datetime
import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect("host=db dbname=postgres user=postgres password=ratestask")

@app.route('/rates')
def get_rates():
    args = request.args
    date_from = args.get('date_from')
    date_to = args.get('date_to')
    origin = args.get('origin')
    destination = args.get('destination')

    if date_from and date_to and origin and destination:

        date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d').date()
        date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()

        if validateDates(date_from, date_to):
            return get_rates_from_db(date_from, date_to,origin,destination)   
        else:  
          return "Invalid Dates", 400    
    else:  
      return "Record not found", 400

def validateDates(date_from, date_to):
    try:
         if date_from <= date_to:
            return True
    except ValueError:
        return False      


def get_rates_from_db(date_from, date_to,origin,destination):
            conn = get_db_connection()
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)    
          
            result = []
            while date_from <= date_to:
                cur.execute("SELECT AVG(p.price) as average_price " + 
                        "FROM  prices as p inner join (SELECT  prices.day from prices "+
                                                        "JOIN ports ON prices.orig_code=ports.code OR prices.dest_code=ports.code "+ 
                                                        "WHERE (prices.orig_code=%s OR ports.parent_slug=%s) "+ 
                                                        "AND (prices.dest_code=%s OR ports.parent_slug=%s)  "+
                                                        "AND prices.day=%s  "+
                                                        "GROUP BY prices.day  "+
                                                        "HAVING COUNT(prices.price) > 3) d on d.day=p.day  "+
                                                        "group by p.day",
                        [origin, origin, destination, destination, date_from]) 
                row = cur.fetchone()        
          
                result_internal = {
                    'day': date_from.strftime('%Y-%m-%d'),
                    'average_price': row[0] if row else "Null",  # if no result found against parameters
                }
                result.append(result_internal)

                date_from = date_from + datetime.timedelta(days=1)

            cur.close()
            conn.close()    
            return result    