// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_msg_srv:msg/MyMsg.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_SRV__MSG__DETAIL__MY_MSG__BUILDER_HPP_
#define MY_MSG_SRV__MSG__DETAIL__MY_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_msg_srv/msg/detail/my_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_msg_srv
{

namespace msg
{

namespace builder
{

class Init_MyMsg_a
{
public:
  Init_MyMsg_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_msg_srv::msg::MyMsg a(::my_msg_srv::msg::MyMsg::_a_type arg)
  {
    msg_.a = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_msg_srv::msg::MyMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_msg_srv::msg::MyMsg>()
{
  return my_msg_srv::msg::builder::Init_MyMsg_a();
}

}  // namespace my_msg_srv

#endif  // MY_MSG_SRV__MSG__DETAIL__MY_MSG__BUILDER_HPP_
