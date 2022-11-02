// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract RSACertification {
    struct Certificate {
        address certificate_owner;
        string user_name;
        string email;
        string phone;
        int256 key_size;
        bytes[] public_key_bytes_array;
        uint256 timestamp;
    }

    mapping(address => Certificate) public userNameToCertificate;

    // create a certificate
    function createCertificate(
        string memory _user_name,
        string memory _email,
        string memory _phone,
        int256 _key_size,
        bytes[] memory _public_key_bytes_array
    ) public {
        userNameToCertificate[msg.sender] = Certificate(
            msg.sender,
            _user_name,
            _email,
            _phone,
            _key_size,
            _public_key_bytes_array,
            block.timestamp
        );
    }

    function getUserName() public view returns (string memory) {
        return userNameToCertificate[msg.sender].user_name;
    }

    function getPhone() public view returns (string memory) {
        return userNameToCertificate[msg.sender].phone;
    }

    function getPublicKey() public view returns (bytes[] memory) {
        return userNameToCertificate[msg.sender].public_key_bytes_array;
    }

    function getTimestamp() public view returns (uint256) {
        return userNameToCertificate[msg.sender].timestamp;
    }
}
