import constants


def return_error(error_msg):
    return ({constants.RESPONSE_MSG_KEY: error_msg}, 400)


def return_success_with_message(msg):
    return ({constants.RESPONSE_MSG_KEY: msg}, 200)
