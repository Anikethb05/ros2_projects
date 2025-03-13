// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_msg_srv:srv/AddThreeNums.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_HPP_
#define MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_msg_srv__srv__AddThreeNums_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_msg_srv__srv__AddThreeNums_Request __declspec(deprecated)
#endif

namespace my_msg_srv
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddThreeNums_Request_
{
  using Type = AddThreeNums_Request_<ContainerAllocator>;

  explicit AddThreeNums_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0.0;
      this->b = 0.0;
      this->c = 0.0;
    }
  }

  explicit AddThreeNums_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0.0;
      this->b = 0.0;
      this->c = 0.0;
    }
  }

  // field types and members
  using _a_type =
    double;
  _a_type a;
  using _b_type =
    double;
  _b_type b;
  using _c_type =
    double;
  _c_type c;

  // setters for named parameter idiom
  Type & set__a(
    const double & _arg)
  {
    this->a = _arg;
    return *this;
  }
  Type & set__b(
    const double & _arg)
  {
    this->b = _arg;
    return *this;
  }
  Type & set__c(
    const double & _arg)
  {
    this->c = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_msg_srv__srv__AddThreeNums_Request
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_msg_srv__srv__AddThreeNums_Request
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddThreeNums_Request_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    if (this->b != other.b) {
      return false;
    }
    if (this->c != other.c) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddThreeNums_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddThreeNums_Request_

// alias to use template instance with default allocator
using AddThreeNums_Request =
  my_msg_srv::srv::AddThreeNums_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_msg_srv


#ifndef _WIN32
# define DEPRECATED__my_msg_srv__srv__AddThreeNums_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_msg_srv__srv__AddThreeNums_Response __declspec(deprecated)
#endif

namespace my_msg_srv
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddThreeNums_Response_
{
  using Type = AddThreeNums_Response_<ContainerAllocator>;

  explicit AddThreeNums_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sum = 0.0;
    }
  }

  explicit AddThreeNums_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sum = 0.0;
    }
  }

  // field types and members
  using _sum_type =
    double;
  _sum_type sum;

  // setters for named parameter idiom
  Type & set__sum(
    const double & _arg)
  {
    this->sum = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_msg_srv__srv__AddThreeNums_Response
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_msg_srv__srv__AddThreeNums_Response
    std::shared_ptr<my_msg_srv::srv::AddThreeNums_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddThreeNums_Response_ & other) const
  {
    if (this->sum != other.sum) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddThreeNums_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddThreeNums_Response_

// alias to use template instance with default allocator
using AddThreeNums_Response =
  my_msg_srv::srv::AddThreeNums_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_msg_srv

namespace my_msg_srv
{

namespace srv
{

struct AddThreeNums
{
  using Request = my_msg_srv::srv::AddThreeNums_Request;
  using Response = my_msg_srv::srv::AddThreeNums_Response;
};

}  // namespace srv

}  // namespace my_msg_srv

#endif  // MY_MSG_SRV__SRV__DETAIL__ADD_THREE_NUMS__STRUCT_HPP_
