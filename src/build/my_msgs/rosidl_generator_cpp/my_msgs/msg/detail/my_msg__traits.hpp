// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_msgs:msg/MyMsg.idl
// generated code does not contain a copyright notice

#ifndef MY_MSGS__MSG__DETAIL__MY_MSG__TRAITS_HPP_
#define MY_MSGS__MSG__DETAIL__MY_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_msgs/msg/detail/my_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const MyMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: a
  {
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MyMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MyMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_msgs

namespace rosidl_generator_traits
{

[[deprecated("use my_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_msgs::msg::MyMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_msgs::msg::MyMsg & msg)
{
  return my_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_msgs::msg::MyMsg>()
{
  return "my_msgs::msg::MyMsg";
}

template<>
inline const char * name<my_msgs::msg::MyMsg>()
{
  return "my_msgs/msg/MyMsg";
}

template<>
struct has_fixed_size<my_msgs::msg::MyMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_msgs::msg::MyMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_msgs::msg::MyMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_MSGS__MSG__DETAIL__MY_MSG__TRAITS_HPP_
