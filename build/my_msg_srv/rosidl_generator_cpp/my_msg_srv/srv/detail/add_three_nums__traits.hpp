// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_msg_srv:srv/AddThreeNums.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__TRAITS_HPP_
#define MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_msg_srv/srv/detail/add_three_nums__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_msg_srv
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddThreeNums_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: a
  {
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << ", ";
  }

  // member: b
  {
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
    out << ", ";
  }

  // member: c
  {
    out << "c: ";
    rosidl_generator_traits::value_to_yaml(msg.c, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddThreeNums_Request & msg,
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

  // member: b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
    out << "\n";
  }

  // member: c
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "c: ";
    rosidl_generator_traits::value_to_yaml(msg.c, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddThreeNums_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_msg_srv

namespace rosidl_generator_traits
{

[[deprecated("use my_msg_srv::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_msg_srv::srv::AddThreeNums_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_msg_srv::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_msg_srv::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_msg_srv::srv::AddThreeNums_Request & msg)
{
  return my_msg_srv::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_msg_srv::srv::AddThreeNums_Request>()
{
  return "my_msg_srv::srv::AddThreeNums_Request";
}

template<>
inline const char * name<my_msg_srv::srv::AddThreeNums_Request>()
{
  return "my_msg_srv/srv/AddThreeNums_Request";
}

template<>
struct has_fixed_size<my_msg_srv::srv::AddThreeNums_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_msg_srv::srv::AddThreeNums_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_msg_srv::srv::AddThreeNums_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace my_msg_srv
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddThreeNums_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: sum
  {
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddThreeNums_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddThreeNums_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_msg_srv

namespace rosidl_generator_traits
{

[[deprecated("use my_msg_srv::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_msg_srv::srv::AddThreeNums_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_msg_srv::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_msg_srv::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_msg_srv::srv::AddThreeNums_Response & msg)
{
  return my_msg_srv::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_msg_srv::srv::AddThreeNums_Response>()
{
  return "my_msg_srv::srv::AddThreeNums_Response";
}

template<>
inline const char * name<my_msg_srv::srv::AddThreeNums_Response>()
{
  return "my_msg_srv/srv/AddThreeNums_Response";
}

template<>
struct has_fixed_size<my_msg_srv::srv::AddThreeNums_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_msg_srv::srv::AddThreeNums_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_msg_srv::srv::AddThreeNums_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_msg_srv::srv::AddThreeNums>()
{
  return "my_msg_srv::srv::AddThreeNums";
}

template<>
inline const char * name<my_msg_srv::srv::AddThreeNums>()
{
  return "my_msg_srv/srv/AddThreeNums";
}

template<>
struct has_fixed_size<my_msg_srv::srv::AddThreeNums>
  : std::integral_constant<
    bool,
    has_fixed_size<my_msg_srv::srv::AddThreeNums_Request>::value &&
    has_fixed_size<my_msg_srv::srv::AddThreeNums_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_msg_srv::srv::AddThreeNums>
  : std::integral_constant<
    bool,
    has_bounded_size<my_msg_srv::srv::AddThreeNums_Request>::value &&
    has_bounded_size<my_msg_srv::srv::AddThreeNums_Response>::value
  >
{
};

template<>
struct is_service<my_msg_srv::srv::AddThreeNums>
  : std::true_type
{
};

template<>
struct is_service_request<my_msg_srv::srv::AddThreeNums_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_msg_srv::srv::AddThreeNums_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__TRAITS_HPP_
