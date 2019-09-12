include_guard(GLOBAL)

function (_get_targets _var _path)
  get_property(_subdirs DIRECTORY ${_path} PROPERTY SUBDIRECTORIES)
  foreach (_subdir IN LISTS _subdirs)
    _get_targets(${_var} ${_subdir})
  endforeach()
  get_property(_targets DIRECTORY ${_path} PROPERTY BUILDSYSTEM_TARGETS)
  foreach (_target IN LISTS _targets)
    get_target_property(_type ${_target} TYPE)
    if(_type STREQUAL STATIC_LIBRARY OR _type STREQUAL INTERFACE_LIBRARY)
      list(APPEND ${_var} ${_target})
    endif()
  endforeach()
  set(${_var} ${${_var}} PARENT_SCOPE)
endfunction()