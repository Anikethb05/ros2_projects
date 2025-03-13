// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_msg_srv:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_SRV__MSG__DETAIL__SPHERE__BUILDER_HPP_
#define MY_MSG_SRV__MSG__DETAIL__SPHERE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_msg_srv/msg/detail/sphere__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_msg_srv
{

namespace msg
{

namespace builder
{

class Init_Sphere_radius
{
public:
  explicit Init_Sphere_radius(::my_msg_srv::msg::Sphere & msg)
  : msg_(msg)
  {}
  ::my_msg_srv::msg::Sphere radius(::my_msg_srv::msg::Sphere::_radius_type arg)
  {
    msg_.radius = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_msg_srv::msg::Sphere msg_;
};

class Init_Sphere_center
{
public:
  Init_Sphere_center()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Sphere_radius center(::my_msg_srv::msg::Sphere::_center_type arg)
  {
    msg_.center = std::move(arg);
    return Init_Sphere_radius(msg_);
  }

private:
  ::my_msg_srv::msg::Sphere msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_msg_srv::msg::Sphere>()
{
  return my_msg_srv::msg::builder::Init_Sphere_center();
}

}  // namespace my_msg_srv

#endif  // MY_MSG_SRV__MSG__DETAIL__SPHERE__BUILDER_HPP_
