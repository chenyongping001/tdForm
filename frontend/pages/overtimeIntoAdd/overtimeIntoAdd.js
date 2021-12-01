import WxValidate from "../../utils/wxValidate"
// pages/overtimeIntoAdd/overtimeIntoAdd.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    form: {
      name: '',
      idcard: '',
      reason: '',
      note: '',
      contact: "",
      contactPhone: "",
      gateValue: 0
    },
    gateItems: [{
        name: '一号门',
        value: 0,
        checked: true
      },
      {
        name: '厂前区',
        value: 1
      }
    ],
    errorMsg: '', // 验证表单显示错误信息
    rules: [{
        name: 'name',
        rules: {
          required: true,
          message: '请填写再入厂人员姓名'
        },
      },
      {
        name: 'idcard',
        rules: {
          required: true,
          message: '请填写再入厂人员身份证号码'
        },
      },
      
      {
        name: 'reason',
        rules: {
          required: true,
          message: '请填写入厂说明'
        }
      },
      {name:"note",rules:{}},
      {name:"gateValue",rules:{range:[0,1],message:'出入门点选择不正确'}},
      {
        name: 'contact',
        rules: {
          required: true,
          message: '请填写电厂联系人姓名'
        },
      },
      {
        name: 'contactPhone',
        rules: [{
          required: true,
          message: '请填写电厂联系人手机号码'
        }, {
          mobile: true,
          message: '电厂联系人手机号码格式不对'
        }]
      },
    ],
  },

  gateChange(e) {
    var gateItems = this.data.gateItems;
        for (var i = 0, len = gateItems.length; i < len; ++i) {
            gateItems[i].checked = gateItems[i].value == e.detail.value;
        }
        this.setData({
            gateItems: gateItems,
            [`form.gateValue`]: e.detail.value
        });
  },
  formInputChange(e) {
    const {
      field
    } = e.currentTarget.dataset
    this.setData({
      [`form.${field}`]: e.detail.value
    })
  },
  // 用第三方工具验证身份证格式
  validateIdcard(idcard) {
    const rules = {
      idcard: {
        required: true,
        idcard: true
      },
    }
    const messages = {
      idcard: {
        required: "请输入身份证号",
      },
    }
    const wxValidate = new WxValidate(rules, messages)
    if (!wxValidate.checkForm(idcard)) {
      const error = wxValidate.errorList[0].msg
      return error
    }
    return null
  },
  weSubmitForm() {
    const idcard = {idcard:this.data.form.idcard}
    const error = this.validateIdcard(idcard)
    if(error){
      this.setData({
        errorMsg:error
      })
      return
    }
    this.selectComponent('#form').validate((valid, errors) => {
      if (!valid) {
        const firstError = Object.keys(errors)
        if (firstError.length) {
          this.setData({
            errorMsg: errors[firstError[0]].message
          })
        }
      }
      else {
        wx.showToast({
          title: '提交成功',
        })
        console.log(this.data.form)
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})