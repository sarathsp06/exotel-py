##exotel-py
Python module for exotels call and sms api's

###installation
`
pip install exotel
`

##Usage
 - Initialize

   ```
   from exotel import Exotel
   client = Exotel(sid,token)
   ```

- make call to connect a number to another
 
   ```
   client.call_number('from_number','exophone','to_number')
   ```

- make call to connect a number to a flow

   ```
   client.call_flow('from_number','exophone','flow_id')
   ```

- send an sms

   ```
   client.sms('from_number',to_number',"sms_body")
   ```

- get details of an sms

   ```
   client.sms_details('sms_sid')
   ```
- get details of a call

   ```
   client.call_details('call_sid')
   ```


##Authors and Contributors

In 2015, Sarath S Pllai ([@sarath_sp06](https://twitter.com/sarath_sp06)) started .Any bug reports would be addressed .Feel free to add more functions and send me the patch with updated README 

##Support or Contact
Having trouble using the library contact me at sarath.sp06@gmail.com
