// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_msgs:srv/AddThreeNums.idl
// generated code does not contain a copyright notice

#ifndef MY_MSGS__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_H_
#define MY_MSGS__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/AddThreeNums in the package my_msgs.
typedef struct my_msgs__srv__AddThreeNums_Request
{
  int64_t a;
  int64_t b;
  int64_t c;
} my_msgs__srv__AddThreeNums_Request;

// Struct for a sequence of my_msgs__srv__AddThreeNums_Request.
typedef struct my_msgs__srv__AddThreeNums_Request__Sequence
{
  my_msgs__srv__AddThreeNums_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_msgs__srv__AddThreeNums_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/AddThreeNums in the package my_msgs.
typedef struct my_msgs__srv__AddThreeNums_Response
{
  int64_t sum;
} my_msgs__srv__AddThreeNums_Response;

// Struct for a sequence of my_msgs__srv__AddThreeNums_Response.
typedef struct my_msgs__srv__AddThreeNums_Response__Sequence
{
  my_msgs__srv__AddThreeNums_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_msgs__srv__AddThreeNums_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_MSGS__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_H_
