month_conversions = {
     "Jan" : "January",
     "Feb" : "Februaary"
}

error_message = "Not a valid value"
print(month_conversions.get("Jan", error_message))
print(month_conversions.get("fe", error_message))