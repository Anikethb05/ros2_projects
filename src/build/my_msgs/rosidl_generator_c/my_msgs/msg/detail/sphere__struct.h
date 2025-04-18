// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_msgs:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef MY_MSGS__MSG__DETAIL__SPHERE__STRUCT_H_
#define MY_MSGS__MSG__DETAIL__SPHERE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'center'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/Sphere in the package my_msgs.
typedef struct my_msgs__msg__Sphere
{
  geometry_msgs__msg__Point center;
  double radius;
} my_msgs__msg__Sphere;

// Struct for a sequence of my_msgs__msg__Sphere.
typedef struct my_msgs__msg__Sphere__Sequence
{
  my_msgs__msg__Sphere * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_msgs__msg__Sphere__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_MSGS__MSG__DETAIL__SPHERE__STRUCT_H_
