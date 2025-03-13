// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_msg_srv:srv/AddThreeNums.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__BUILDER_HPP_
#define MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_msg_srv/srv/detail/add_three_nums__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_msg_srv
{

namespace srv
{

namespace builder
{

class Init_AddThreeNums_Request_c
{
public:
  explicit Init_AddThreeNums_Request_c(::my_msg_srv::srv::AddThreeNums_Request & msg)
  : msg_(msg)
  {}
  ::my_msg_srv::srv::AddThreeNums_Request c(::my_msg_srv::srv::AddThreeNums_Request::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_msg_srv::srv::AddThreeNums_Request msg_;
};

class Init_AddThreeNums_Request_b
{
public:
  explicit Init_AddThreeNums_Request_b(::my_msg_srv::srv::AddThreeNums_Request & msg)
  : msg_(msg)
  {}
  Init_AddThreeNums_Request_c b(::my_msg_srv::srv::AddThreeNums_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_AddThreeNums_Request_c(msg_);
  }

private:
  ::my_msg_srv::srv::AddThreeNums_Request msg_;
};

class Init_AddThreeNums_Request_a
{
public:
  Init_AddThreeNums_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddThreeNums_Request_b a(::my_msg_srv::srv::AddThreeNums_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_AddThreeNums_Request_b(msg_);
  }

private:
  ::my_msg_srv::srv::AddThreeNums_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_msg_srv::srv::AddThreeNums_Request>()
{
  return my_msg_srv::srv::builder::Init_AddThreeNums_Request_a();
}

}  // namespace my_msg_srv


namespace my_msg_srv
{

namespace srv
{

namespace builder
{

class Init_AddThreeNums_Response_sum
{
public:
  Init_AddThreeNums_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_msg_srv::srv::AddThreeNums_Response sum(::my_msg_srv::srv::AddThreeNums_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_msg_srv::srv::AddThreeNums_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_msg_srv::srv::AddThreeNums_Response>()
{
  return my_msg_srv::srv::builder::Init_AddThreeNums_Response_sum();
}

}  // namespace my_msg_srv

#endif  // MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__BUILDER_HPP_
