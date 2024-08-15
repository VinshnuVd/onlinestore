from rest_framework.views import exception_handler


# Formats the Response
def response_writer(status=200,data=None,message=None,error=None):
	response = {}
	response['status'] = str(status)
	if data != None:
			response['data'] = data
	if message:
			response['message'] = message
	if error:
			response['error_description'] = error
	return response


# Handles Unhandled Exception in Views
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:

        # remove the initial value
        response.data = {}
        errors = []

        # serve status code in the response
        response.data['status'] = response.status_code

        # check if exception has dict items
        if hasattr(exc.detail, 'items'):
            for key, value in exc.detail.items():
                errors.append("{}".format("".join(value)))
        else:
            errors = exc.detail
        
        if len(errors) != 0:
            response.data['error_description'] = errors

    return response